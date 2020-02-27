from hashtable import hashtable


class Set:
    '''A hash table data structure that implements a set abstract data type.'''
    def __init__(elements=None):
        '''Create a new set structure, and add elements if it is given.'''
        # property that tracks the number of elements in constant time
        self.size = 0 if elements is None else len(elements)

    def contains(element):
        '''Returns a boolean indicating whether element is in this set'''
        pass

    def add(element):
        '''Add element to this set, if not present already.'''
        pass

    def remove(element):
        '''Remove element from this set, if present, or else raise KeyError.'''
        pass

    def union(other_set):
        '''Returns a new set that is the union of this set and other_set.'''
        pass

    def intersection(other_set):
        '''Returns a new set that is the intersection of self and other_set.'''
        pass

    def difference(other_set):
        '''Returns a new set that is the difference of self and other_set.'''
        pass

    def is_subset(other_set):
        '''Returns a boolean for whether other_set is a subset of self.'''
        pass
