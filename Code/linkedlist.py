#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes.

        """
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
           This method runs in constant time, otherwise represented as O(1), in
           all scenarios. This is because all we do is retrieve the value
           stored in the size property of the given LinkedList instance.

        """
        return self.size

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
           raise ValueError if the given index is out of range of the list size.

           Best case running time: O(1)
           This method runs in constant time if we are getting the item at the
           index 0 (also can be thought of as the head node), or if the index is
           out of range of the list. In the former, this is because we only need
           one iteration through the for loop. In the latter, it is because we can
           be sure we will need no iteration of the for loop, and just raise the
           ValuError exception.

           Worst case running time: O(n)
           This occurs if we are trying to get the item at the last index
           position in the list, otherwise referred to as the tail node. This is
           because we will need to traverse through all the items in the list,
           which increases in linear time with respect to the growth of items in
           the list, which is represented by n.

        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # Find the node at the given index
        node = self.head
        for i in range(index):
            node = node.next
        # return its data
        return node.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
           raise ValueError if the given index is out of range of the list
           size.

           Best case running time: O(1)
           This function mimics the approach of the prepend and append methods
           in several scenarios: if we are inserting an item at the head node
           position (which is index 0), this uses the runtime of the prepend
           method; or if we inserting at the tail node, or we are inserting an
           item into a list with no other items, this method uses the same
           runtime as the append operation (in the latter case, the index
           would also be equal to 0). Furthermore, this method also runs in
           constant time if the index is out of range, in which it takes
           constant time to raise tbe ValueError.

           Worst case running time: O(n)
           If we are inserting an item at an index position that cannot be
           considered the head nor the tail, then we have a variable number
           of items to iterate over. In the worst case scenario, the index we
           want to insert at is just before the tail, meaning we need n-1
           iterations through the for loop (found in the else block below),
           where n is the number of items in the list. The runtime in this
           scenario scales in linear time to the growth of the list, therefore
           we disregard the -1 and are left with O(n) runtime.

        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # if we are inserting at the tail, or no previous nodes, then append
        if self.size == index:
            self.append(item)
        # if we are inserting at the head, then just perform a prepend
        elif index == 0:
            self.prepend(item)
        else:
            # Perform traversal of the nodes
            prev_node = self.head
            # find the node at index, as well as the one just before it
            for i in range(index - 1):
                prev_node = prev_node.next
            node_being_moved = prev_node.next
            # make a new Node for the data to be inserted
            new_node = Node(item)
            # insert the new node at the index, and connect it to the rest
            prev_node.next = new_node
            new_node.next = node_being_moved
            # increment the size property
            self.size += 1

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]

        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.tail = new_node
        # Increment the size property
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node
        # Increment the size property
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Start at the head node
        node = self.head
        # traverse the nodes to find old_item
        while node is not None:
            # Check if this node's data matches the old_item
            if node.data == old_item:
                # We found the node, now change the data it references
                node.data = new_item
                # end the method by returning None
                return None
            else:
                # Skip to the next node
                node = node.next
        # old_item is not in the list, so raise a ValuError
        raise ValueError(f'Item not in list: {old_item}')

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while found is False and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found is True:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node
                    previous.next = None
                # Update tail to the previous node regardless
                self.tail = previous
            # Decrement the size property
            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
