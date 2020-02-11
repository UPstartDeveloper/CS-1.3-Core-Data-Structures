#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.length() == 0

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
           Running time: O(1)
           This method does nothing more than an prepend() operation, found in
           the LinkedList class. This method in turn performs an O(1) operation
           because since we have a pointer to the head, we do not need a
           variable number of iterations through the list to find where we need
           to add in the new item.

        """
        self.list.prepend(item)  # the tail is the top of this Stack

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty() is True:
            return None
        else:
            return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
           or raise ValueError if this stack is empty.
           Running time: O(1)
           The runtime and space complexity of this method is independent of
           the size of the list. It first checks the size of the list against
           0, which runs in constant time because the list has a property for
           its size that is used for the comparision. From there, the average
           case will be that our stack is not empty, and therefore we simply
           have to get the item from head data.

        """
        if self.is_empty() is False:
            top_item = self.list.head.data
            self.list.delete(top_item)
            return top_item
        else:
            raise ValueError('No items in this stack.')


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
           Running time: O(n)
           This method performs an append() operation on the built-in list
           object in Python, which can be considered as a dynamic array data
           structure. There exist two possible runtimes for list.append(). In
           one scenario when the list has not yet run out of allocated memory
           spaces, it simply populates the new item at the index position
           equal to the length of the array (which it keeps track) - a constant
           runtime operation.
           In the other scenario the list tries to add the new item, but it
           cannot due to having already running out of allocated memory spaces
           that are contiguous. Therefore, the processor needs to go and find
           another block of memory that is larger, copy over all the elements
           in the existing array, and then it can add the new item. Since this
           algorithm involves a traversal through the list (while copying
           items over), the complexity of this operation is in linear time.

           Taken together, the overall runtime complexity of this append()
           operation averages to O(n), because it will grow in direct
           proportion to the number of items in the list.

        """
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty() is True:
            return None
        else:
            return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
           or raise ValueError if this stack is empty.
           Running time: O(1)
           Whether or not the list is empty, this operation will decide in
           constant time; because the Python list data type keeps track of its
           size as a property of the object. From there, the method will either
           raise a ValueError exception, or calulate the index of the index in
           the array it needs to remove an element from, remove the element at
           that position, and return it. Neither of these processes contains
           any steps which have a variable runtime, therefore the overall
           method will run in constant time asymptotically.

        """
        if self.is_empty() is True:
            raise ValueError('No items in this stack.')
        else:
            return self.list.pop(-1)


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
