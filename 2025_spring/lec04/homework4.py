
def list_to_dict(input_list):
    '''
    This function should return a dictionary in which each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`. 
    '''
    output_dict = {}
    for n, x in enumerate(input_list):
        output_dict[n] =x
    return output_dict




