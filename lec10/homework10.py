import numpy as np
import torch
import torch.nn as nn

def get_features(waveform, Fs):
    '''
    Get features and labels from a waveform.
    '''

    # ---------- Pre-emphasis ----------
    pre_emphasis = 0.97
    waveform = np.append(waveform[0], waveform[1:] - pre_emphasis * waveform[:-1])

    # ---------- Spectrogram parameters ----------
    frame_len = int(0.004 * Fs)   # 4 ms
    step = int(0.002 * Fs)        # 2 ms

    N = len(waveform)
    num_frames = 1 + (N - frame_len) // step

    frames = np.zeros((num_frames, frame_len))
    for i in range(num_frames):
        start = i * step
        frames[i] = waveform[start:start + frame_len]

    # FFT magnitude
    spectrum = np.abs(np.fft.fft(frames, axis=1))

    # Keep low-frequency (non-aliased) half
    features = spectrum[:, :frame_len // 2]

    # ---------- VAD for labels ----------
    vad_frame_len = int(0.025 * Fs)  # 25 ms
    vad_step = int(0.010 * Fs)       # 10 ms

    num_vad_frames = 1 + (N - vad_frame_len) // vad_step
    energies = []

    for i in range(num_vad_frames):
        start = i * vad_step
        frame = waveform[start:start + vad_frame_len]
        energies.append(np.sum(frame ** 2))

    energies = np.array(energies)
    threshold = 0.1 * np.max(energies)

    labels = -1 * np.ones(num_frames, dtype=int)

    current_label = 0
    for i, energy in enumerate(energies):
        if energy > threshold:
            start = i * vad_step
            end = start + vad_frame_len

            # Convert time range to feature-frame indices
            start_f = int(start / step)
            end_f = int(end / step)

            labels[start_f:end_f] = current_label
            current_label += 1

    # Remove silent frames
    mask = labels >= 0
    features = features[mask]
    labels = labels[mask]

    # Repeat each label five times
    labels = np.repeat(labels, 5)
    features = np.repeat(features, 5, axis=0)

    return features, labels


def train_neuralnet(features, labels, iterations):
    '''
    Train a simple neural network classifier.
    '''

    X = torch.tensor(features, dtype=torch.float32)
    y = torch.tensor(labels, dtype=torch.long)

    NFEATS = X.shape[1]
    NLABELS = int(labels.max()) + 1

    # Model
    model = nn.Sequential(
        nn.LayerNorm(NFEATS),
        nn.Linear(NFEATS, NLABELS)
    )

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    lossvalues = np.zeros(iterations)

    for i in range(iterations):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        lossvalues[i] = loss.item()

    return model, lossvalues


def test_neuralnet(model, features):
    '''
    Test the trained neural network.
    '''

    X = torch.tensor(features, dtype=torch.float32)

    with torch.no_grad():
        outputs = model(X)
        probabilities = torch.softmax(outputs, dim=1)

    return probabilities.detach().numpy()
