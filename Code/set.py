from hashtable import HashTable


class Set:
    '''A hash table data structure that implements a set abstract data type.'''
    def __init__(self, elements=None):
        '''Create a new set structure, and add elements if it is given.'''
        # property that tracks the number of elements in constant time
        self.size = 0
        # initialize collection propoerty of the set
        if elements is None:
            self.collection = HashTable()
        else:
            self.collection = HashTable(len(elements))
            for element in elements:
                self.add(element)

    def contains(self, element):
        """Returns a boolean indicating whether element is in this set.

           This method runs at O(1) amortized runtime complexity. The runtime
           depends upon the time it takes to traverse the hash buckets
           of the self.collection HashTable object. This class is dynamically
           resizing the number of hash buckets in order to keep the load factor
           to a small constant value, so on average we can say the the runtime
           of this operation is constant.

        """
        return self.collection.contains(element) is True

    def add(self, element):
        """Add element to this set, if not present already.

           This methods runs in O(n) time where n is the number of set
           elements. This is because we require checking to make sure the
           element is not already is tbe set. This in turns necessitates us
           checking the element for its membership in a list of all the entries
           in the self.collection property. The runtime of gathering a list of
           all elements scales in linear magnitude with the number of elements.

        """
        if self.contains(element) is False:
            self.collection.set(element, None)
            self.size += 1

    def remove(self, element):
        """Remove element from this set, if present, or else raise KeyError.

           The runtime of this method asymptotically scales with respect with
           the runtime required to traverse the appropiate hash bucket of the
           self.collection object, searching for the element to delete. The
           runtime of this step in turn depends on the load factor. The
           HashTable class is used to implement self.collection and it is
           dynamically resizing, so the load factor is kept to a small value.
           Therefore we can express the runtime of this method using O(1)
           amortized.

        """
        self.collection.delete(element)
        self.size -= 1

    def union(self, other_set):
        """Returns a new set that is the union of this set and other_set.

           The runtime of this method depends on the number of elements in two
           different sets, which we can represent using the variables n1 and
           n2 respectively. Since we iterate over the elements of these two
           sets in two separate steps, we can add them up for an overall method
           runtime complexity of O(n1 + n2).

        """
        # gather items from both SetTests
        items_from_self = self.collection.keys()
        items_from_other = other_set.collection.keys()
        # initialize a new Set object
        new_set = Set()
        # add the items to the new set as appropiate
        for item in items_from_self:
            new_set.add(item)
        for item in items_from_other:
            if new_set.contains(item) is False:
                new_set.add(item)
        return new_set

    def intersection(self, other_set):
        """Returns a new set that is the intersection of self (the calling set)
           and other_set.

          The runtime of this method is O(n), where n denotes the number of
          elements in whichever of the sets is smaller than the other,
          and defaults to self in cases when the set objects have an equal
          amount of elements. This is due to needing to iterate over the list
          of elements in this set, in order to check if they are present in
          the other set.

        """
        # initialize a set to return
        return_set = Set()
        # decide which of the sets is smaller
        pull_from_set = None
        if self.size <= other_set.size:
            pull_from_set = self
        else:
            # if other_set is smaller, ensure sets compared are different
            pull_from_set = other_set
            other_set = self
        # add the appropiate elememts into the set to be returned
        for element in pull_from_set.collection.keys():
            if other_set.contains(element) is True:
                return_set.add(element)
        return return_set

    def difference(self, other_set):
        """Returns a new set that is the difference of self and other_set.

           The runtime complexity of Set.difference is asymptotically
           determined by the list comprehension below. This operation filters
           out any elements in the set of self, if they are also found in the
           set of other_set. If we represent the numbers of elements in self
           and other_set using n1 and n2 respectively, then we can say that
           this list comprehension is performing a linear search of n2
           iterations, for each of its n1 iterations.

           Therefore we can conclude that the runtime of this method is
           O(n1 * n2).

        """
        # store the elements found in both sets in separate lists
        self_elem = self.collection.keys()
        other_elem = other_set.collection.keys()
        # remove elements from the set of self, if they are found in other_set
        unique_elements = [
            elem for elem in self_elem if elem not in other_elem
        ]
        # initialize a set to return
        return Set(unique_elements)

    def is_subset(self, other_set):
        """Returns a boolean for whether other_set is a subset of self.
           Similar to the runtime of Set.union, the runtime of this method is
           determined by having to store separate lists of the elements in
           the self set and other_set. The numbers of elements in these sets
           can be represented using the variables n1 and n2 respectively. Since
           we iterate over the elements of these two
           sets in two separate steps, we can add them up for an overall method
           runtime complexity of O(n1 + n2).

        """
        # store the elements found in both sets in separate lists
        self_elem = self.collection.keys()
        other_elem = other_set.collection.keys()
        # iterate through the elements in other_set
        for element in other_elem:
            # check of they are present in the set of self
            if element not in self_elem:
                return False
        return True
