#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.length() == 0

    def length(self):
        """Return the number of items in this queue."""
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
           Running time: O(1)
           This method runs in constant runtime; because the LinkedList class
           uses a tail pointer to be able to find where it needs to add a new
           item, without any variable number of iterations through the list.

        """
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty() is True:
            return None
        else:
            return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
           or raise ValueError if this queue is empty.
           Running time: O(1)
           The queue does not need to take into account the growing number of
           the items in the list in order to run. This is because we can only
           remove the item at the front of the list in a queue; therefore we
           need only to remove the found by using the head pointer of the
           LinkedList class, or we raise a ValueError if the list is empty.
           Therefore, the runtime of the method is constant, meaning it will
           not be affected asymptotically by changes in the size of the list.

        """
        if self.is_empty() is True:
            raise ValueError('There are no items in this queue.')
        else:
            front = self.front()
            self.list.delete(front)
            return front


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
           Running time: O(n)
           The runtime of this method is mainly dependent on the space and time
           complexity of the append operation in Python's built-in list object.
           This complexity averages out to O(n) on average. The list object is
           a dynamic array, meaning we will always be able to add new items (as
           long as there is RAM available) - yet when we run out of allocated
           memory, this operation has to traverse through all the items in the
           list, as it copies them over to a new block of contiguous memory
           that satisfies the size requirements. Due to step running in linear
           time, we can describe the complexity of this method increasing in
           linear scale, with respect to the growth of the number of items in
           the list.

        """
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty() is True:
            return None
        else:
            return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
           or raise ValueError if this queue is empty.
           Running time: O(n)
           In the average case, we will have a non-empty list and need to
           remove the item at the first index position. Thereafter, every item
           in the list must shift one index to the one previous it in the order
           of memory addresses. In total this will mean a complete traversal
           through the list. Therefore the complexity of this method rises in
           direct proportion to the growth of the number of items in the list.
           After all if our list doubled in size, wouldn't we need twice as
           many iterations to traverse it?

        """
        if self.is_empty() is True:
            raise ValueError('There are no items in this queue.')
        else:
            return self.list.pop(0)


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
