from hashtable import HashTable


class Set:
    '''A hash table data structure that implements a set abstract data type.'''
    def __init__(self, elements=None):
        '''Create a new set structure, and add elements if it is given.'''
        # property that tracks the number of elements in constant time
        self.size = 0
        # init collection propoerty of the set
        if elements is None:
            self.collection = HashTable()
        else:
            self.collection = HashTable(len(elements))
            for element in elements:
                self.add(element)

    def contains(self, element):
        '''Returns a boolean indicating whether element is in this set'''
        return self.collection.contains(element) is True

    def add(self, element):
        '''Add element to this set, if not present already.'''
        self.collection.set(element, None)
        self.size += 1

    def remove(self, element):
        '''Remove element from this set, if present, or else raise KeyError.'''
        pass

    def union(self, other_set):
        '''Returns a new set that is the union of this set and other_set.'''
        pass

    def intersection(self, other_set):
        '''Returns a new set that is the intersection of self and other_set.'''
        pass

    def difference(self, other_set):
        '''Returns a new set that is the difference of self and other_set.'''
        pass

    def is_subset(self, other_set):
        '''Returns a boolean for whether other_set is a subset of self.'''
        pass
