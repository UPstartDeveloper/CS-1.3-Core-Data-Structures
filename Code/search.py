#!python


import string


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def is_less_than(elem, item):
    """Determine if the elem is less than item.

       Parameters:
       elem: str or int or float value
       item: str or int or float value

       Return: bool

    """
    # a list of lowercase English letters
    alpha = list(string.ascii_lowercase)
    # determine if the elem is a str or number
    if isinstance(elem, str) is True:
        # if an English letter, less than or greater than is by index in alpha
        index_elem = linear_search_recursive(elem[0].lower(), alpha)
        index_item = linear_search_recursive(item[0].lower(), alpha)
        return (index_elem < index_item)
    else:
        # if a number, then determine greater than or less than normally
        return (elem < item)


def calculate_middle(low, high):
    '''Return the index of the middle, given lowest and highest indices.'''
    return ((low + high) // 2)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # init index to start at middle of the array
    low = 0
    high = (len(array) - 1)
    mid = calculate_middle(low, high)
    # init the list element to start looking at
    elem = array[mid]
    # continually move the mid_index around, until you find the item
    while not elem == item and not (low == mid or mid == high):
        # determine if the element is less than or greater than item
        if is_less_than(elem, item) is True:
            # cut out the lower half of the list
            low = mid
            mid = calculate_middle(low, high)
        else:
            # cut out the upper half of the list
            high = mid
            mid = calculate_middle(low, high)
        # reassign element using new middle
        elem = array[mid]
        # if elem now matches item, return the middle index here
        if elem == item:
            return mid
    # if the item is found right at the middle
    else:
        return mid
    # return value for when item not in list
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
