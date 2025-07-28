

def cancellation(input_List, stop_word):
    '''
    Copy elements one by one from input_list into output_list. 
    If one of the elements is equal to the stop_word, then stop the function,
    and return what you have so far.
    '''
    output_List = []
    for element in input_List:
        if element == stop_word:
            break
        output_List.append(element)
    return output_List 
        
def copy_all_but_skip_word(input_List, skip_word):
    '''
    This function should copy elements one by one from input_list into output_list.
    If one of the elements is equal to the skip_word, then you should skip that element,
    but keep checking all of the other elements.
    '''
    output_List = []
    for element in input_List:
        if element == skip_word:
           continue
        output_List.append(element)
    return output_List

def my_average(input_List):
    '''
    You may assume that `input_list` is a non-empty list, in which every element is a number.  
    Calculate the average value, and return it. 
    '''
    number_of_elements = len(input_List)
    sum_of_elements = 0
    for element in input_List:
        sum_of_elements = sum_of_elements + element
    return sum_of_elements / number_of_elements


