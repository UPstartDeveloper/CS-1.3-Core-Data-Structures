#!python


import string


def linear_search(array, item):
    """Return the first index of item in array or None if item is not found

       Runtime Analysis:
       Given n as the number of items in the array, linear search runs in
       linear time. In the best case we find the item at the first index
       in the array, which can be expressed as O(1) iterations. In the worst
       case the item is not found in the array, which can be expressed as
       O(n) iterations.

       Spacetime Analysis:
       This function uses O(n) space on average. The amount of memory used by
       this algorithm comprises only of local variables. The amount of data
       used up by these variables grows directly proportional with respect to
       the size of the array. If we double the size of array, we would
       asymptotically need twice as many variables to search through it, using
       linear search.

    """
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
    """Return the index of item in sorted array or None if item is not found.

       Runtime Analysis:
       On each iteration or recursive step through this function, half of the
       list elements are eliminated from consideration. On the best case, the
       item is found exactly at the middle index position in the array. This is
       expressed at O(1). On the worst case, the item is not found, or is just
       one index postion off to the left or right of the middle index position.
       Because I use linear search as a helper function in this implementation
       (to handle alphabetization), this case is expressed as O(n*log(n)), or
       more simply O(n) asymptotically. That is to say, although usually binary
       search would be only O(log(n)) complexity, since I am using this
       function to handle both numbers and str values, it is O(n).

       Spacetime Analysis:
       Since this implementation uses linear search, it shares the same
       spacetime complexity as the linear search implementation above: O(n).

    """
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def calculate_middle(low, high):
    '''Return the index of the middle, given lowest and highest indices.'''
    return ((low + high) // 2)


def binary_search_iterative(array, item):
    # init index to start at middle of the array
    low = 0
    high = len(array)
    mid = calculate_middle(low, high)
    # init the list element to start looking at
    elem = array[mid]
    # continually move the mid_index around, until you find the item
    while not elem == item:
        # determine if the element is less than or greater than item
        if elem < item:
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
        if elem < item:
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
