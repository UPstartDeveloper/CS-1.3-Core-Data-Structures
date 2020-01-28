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
    # base cases
    if index >= len(array):
        return None
    if array[index] == item:
        return index
    # recursive process
    else:
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def compare_letters(elem, item):
    '''Given two strings, return which comes first alphabetically.'''
    # a list of lowercase English letters
    alpha = list(string.ascii_lowercase)
    # init indices used to track letters
    index = 0
    elem_length = len(elem)
    item_length = len(item)
    # avoid IndexError
    while not index >= elem_length or index >= item_length:
        # compare letters at the same index in the words
        value_elem = linear_search_recursive(alpha, elem[index].lower())
        value_item = linear_search_recursive(alpha, item[index].lower())
        # if one of the values is less than the other, for alphabetization
        if value_elem < value_item:
            return True
        elif value_elem > value_item:
            return False
        else:
            # if we compared equal letters, then move on to the next letter
            index += 1
    # if both words equal up to n letters, then alphabetize based on length
    return (elem_length < item_length)


def is_less_than(elem, item):
    """Determine if the elem is less than item.

       Parameters:
       elem: str or int or float value
       item: str or int or float value

       Return: bool

    """
    # determine if the elem is a str or number
    if isinstance(elem, str) is True:
        # lesser value comes first alphabetically
        less_than = compare_letters(elem, item)
        return (less_than is True)
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
    high = len(array)
    mid = calculate_middle(low, high)
    # init the list element to start looking at
    elem = array[mid]
    # continually move the mid_index around, until you find the item
    while not elem == item:
        # determine if the element is less than or greater than item
        if is_less_than(elem, item) is True:
            # cut out the lower half of the list,
            low = mid
        else:
            # cut out the upper half of the list
            high = mid
        mid = calculate_middle(low, high)
        # reassign element using new middle, and check again
        elem = array[mid]
        if low == mid and not elem == item:
            return None
    # if the item is found right at the middle
    else:
        return mid
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # for the first pass only, init left and right (same as low and high)
    if left is None and right is None:
        left = 0
        right = len(array)
    # retireve the element at the middle index
    mid = calculate_middle(left, right)
    elem = array[mid]
    # check if we have found the element
    if elem == item:
        return mid
    else:
        # decide how to move the indices, and try again
        if is_less_than(elem, item) is True:
            # cut out the lower half of the list
            left = mid
        else:
            # cut out the upper half of the list
            right = mid
        mid = calculate_middle(left, right)
        elem = array[mid]
        # if we are checking indices again, the item's not present
        if left == mid and not elem == item:
            return None
        # call the function with the new subset of the list
        return binary_search_recursive(array, item, left, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
