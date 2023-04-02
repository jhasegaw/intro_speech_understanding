# intro_speech_understanding

This repository contains assignments for the KCGI graduate course
"Intro to Speech Understanding."  Recommended use:

    #. Clone the course directory by typing:

```
git clone https://github.com/jhasegaw/intro_speech_understanding
```

This will create the directory `intro_speech_understanding`, and will
fill it with all of the code and assignments that have been published so far.

    #. Every week, before lecture, `cd` to the directory
`intro_speech_understanding`, and then do the following:

```
git add -A
git commit -m "comment"
git fetch
git merge -m "comment"
```

The command `git add -A` creates a new local record of your work, and
`git commit -m "comment"` puts the local record into your local
history.  By putting your work into your local history, you have made
it possible to use git to recover your file, even if you accidentally
delete it.

The command `git fetch` fetches the new assignments from github.  The
command `git merge -m "comment"` merges the downloaded assignments,
together with your own work, into the directory that's visible on your
own machine.

If you have edited a file, and if the github repository has also
edited the same file, then `git` will open a text editor (probably <a
href="https://www.cs.colostate.edu/helpdocs/vi.html">vi</a>), and show
you the conflicting edits.  You'll need to decide how to resolve each
conflict, and then save the file.

