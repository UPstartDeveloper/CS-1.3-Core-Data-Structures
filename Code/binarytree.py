#!python
from queue import Queue
from stack import Stack


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.left is not None or self.right is not None

    def count_edges(self, direction):
        """Count the height of a node going to the left, or to the right.

           Parameter:
           direction(str): determines whether the method will judge the height
                           of a Node depending on its descendants on the left
                           or right

            Returns:
            int: the height of the Node whose height is being measured, from
                 just the left or right side

        """
        if self.is_leaf() is True:
            return 0
        elif direction == 'left' or self.right is None:
            return 1 + self.left.count_edges('left')
        elif direction == 'right' or self.left is None:
            return 1 + self.right.count_edges('right')

    def height(self):
        """Return the height of this node (the number of edges on the longest
           downward path from this node to a descendant leaf node).

           Best and worst case running time: O(l), where l is the number of
           levels in the tree. This is under the condition that our tree is
           balanced, and we are taking the height of the root, the node of
           greatest height. The runtime of this method scales with the number
           of levels it must reach down to find the furthest leaf node.

        """
        # Check if left child has a value and if so calculate its height
        left_height = 0
        if self.left is not None:
            left_height += self.count_edges('left')
        # Check if right child has a value and if so calculate its height
        right_height = 0
        if self.right is not None:
            right_height += self.count_edges('right')
        # Return one more than the greater of the left height and right height
        if left_height > right_height:
            return (left_height)
        else:
            return (right_height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
          downward path from this tree's root node to a descendant leaf node).

          Best and worst case running time: O(l), where l is the number of
          levels in our tree. This is under the condition our tree is balanced,
          meaning that is has the minimum number of levels needed to store all
          of the nodes (represented by n), in which case we could also express
          this using O(log(n)). We need the total number of levels in the tree,
          because we always measure the height of a tree using the height of
          the root node.

        """
        if self.root is not None:
            return self.root.height()
        return self.root

    def contains(self, item):
        """Return True if this binary search tree contains the given item.

           Best case running time: O(1), if the item we are searching for is
           encapsulated by the root node.

           Worst case running time: O(log(n)), if the item we are searching
           for is encapsulated by one of the leaves in the tree. In this case
           we must rely on the worst case of the binary search algorithm,
           which will cut down the size of possibilities by 2 on every
           recursive call.

        """
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
           or None if the given item is not found.

           Best case running time: O(1)
           Similar to the contains() method, we rely on the best case runtime
           of the binary search algorithm, where the item we are searching for
           is located at the root of the tree.

           Worst case running time: O(log(n)), where n is the number of nodes
           in the tree. This is if the item we're searching for is located at
           one of the leaves in the tree.

        """
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node data if found, or node if it's None
        return node.data if node is not None else node

    def insert(self, item):
        """Insert the given item in order into this binary search tree.

           Best case running time:
           In the best case we are inserting a node into a tree that is
           previously empty. In this case our runtime is O(1), because we only
           need to construct a new BinaryTreeNode object and point to it using
           the BinarySearchTree root property.

           Worst case running time:
           In the worst case we will need to traverse several levels of the
           tree before we have a spot to add the new BinaryTreeNode. The
           complexity of this step will scale in proportion to O(l), the number
           of levels that previously exist in the tree.

        """
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = BinaryTreeNode(item)
            # Increase the tree size
            self.size += 1
            return None
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_iterative(item)
        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            # Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        # Check if the given item should be inserted right of parent node
        elif item > parent.data:
            # Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        # Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search
           tree, or None if the given item is not found. Search is performed
           iteratively starting from the root node.

           Best case running time: O(1), if the item we are searching for is
           encapsulated by the root node.

           Worst case running time: O(log(n)), if the item we are searching
           for is encapsulated by one of the leaves in the tree. In this case
           the runtime of this method scales in direction proportion to the
           number of levels previously existing in the tree.

        """
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search
           tree, or None if the given item is not found. Search is performed
           recursively starting from the given node (give the root node to
           start recursion).

           Best case running time: O(1), if the item we are searching for is
           encapsulated by the root node.

           Worst case running time: O(log(n)), if the item we are searching
           for is encapsulated by one of the leaves in the tree. In this case
           the runtime of this method scales in direction proportion to the
           number of levels previously existing in the tree.

        """
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
           (or the parent node of where the given item would be if inserted)
           in this tree, or None if this tree is empty or has only a root node.

           Search is performed iteratively starting from the root node.

           Best case running time: O(1), if the item we are searching for is
           encapsulated by the root node.

           Worst case running time: O(log(n)), if the item we are searching
           for is encapsulated by one of the leaves in the tree. In this case
           the runtime of this method scales in direction proportion to the
           number of levels previously existing in the tree.

        """
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, updates, parent
            return self._find_parent_node_recursive(item, node.left, node)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, updates parent
            return self._find_parent_node_recursive(item, node.right, node)

    def find_direction(self, node, parent):
        '''Return whether the node is to the left or right of its parent.'''
        if parent.left == node:
            return 'left'
        elif parent.right == node:
            return 'right'
        # error case: if the node is not actually the child of the parent
        raise ValueError('The node is not the child of the parent.')

    def promote_descendants(self, node, parent, direction=None):
        """Takes the descendants on the left, raise them to the parent's place.

           Parameters:
           node(BinaryTreeNode): the node being deleted that's not the root,
                                 and has 2 children
           parent(BinaryTreeNode): the parent of the node being deleted
           direction_from_parent(str): indicates if the node being deleted is
                                       to the left or right of the parent
        """
        while node.left is not None:
            moving_up = node.left
            if parent is not None and direction is None:
                direction = self.find_direction(node, parent)
            if direction == 'left':
                parent.left = moving_up
            elif direction == 'right':
                parent.right = moving_up
            moving_up.right = node.right
            parent = node
            node = node.left

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.

           Best case running time: O(1)
           This is if we are trying to delete from an empty tree, because then
           we require the minimum number of iterations to "find" the node, and
           then constant runtime to raise a ValuError exception.

           Worst case running time: O(l)
           This is if we are deleting item at the root node, which has two
           children nodes. Under the conditions that we have a balanced tree
           with the minimum number of levels, and that the predecessor or
           successor we need to replace the root is one of the leaves of the of
           the tree, then the runtime of this operation will scale with the
           number of levels pre-existing levels in the tree.

        """
        node = self._find_node_recursive(item, self.root)
        if node is None:
            # raise ValueError because node is not present
            raise ValueError('Item is not present in this binary tree.')
        else:
            # decrement the size of the tree
            self.size -= 1
            # find the parent, and whether this node is to its left or right
            parent = self._find_parent_node_iterative(node.data)
            direction_from_parent = ''
            if parent is not None:
                direction_from_parent = self.find_direction(node, parent)
            # node has 0 children
            if node.is_leaf() is True:
                # if this is the last node, delete the root
                if parent is None:
                    self.root = None
                # set the appropiate child property of the parent to None
                elif direction_from_parent == 'left':
                    parent.left = None
                else:
                    parent.right = None
                return None
            elif node.is_branch() is True:
                # node has 2 children
                if node.left is not None and node.right is not None:
                    # node is the root
                    if self.root == node:
                        # change the root
                        self.root = self.root.left
                        # move the descendants
                        self.promote_descendants(node, None)
                    else:
                        # only move the descendents
                        self.promote_descendants(node, parent,
                                                 direction_from_parent)
                    return None
                # node has 1 child - check if it's to the left
                elif node.left is not None:
                    # if we mere;y need to change the root
                    if parent is None:
                        self.root = node.left
                    # now decide which of the parent's pointers to connect with
                    elif direction_from_parent == 'left':
                        parent.left = node.left
                    else:
                        parent.right = node.left
                # the 1 child is on the right side
                elif node.right is not None:
                    # if we mere;y need to change the root
                    if parent is None:
                        self.root = node.right
                    # now decide which of the parent's pointers to connect with
                    elif direction_from_parent == 'left':
                        parent.left = node.right
                    else:
                        parent.right = node.right

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
           Start at the given node and visit each node with the given function.

           Running time: O(n), where n is the number of nodes in the tree.
           This is under the conditions that the tree is balanced, where each
           node has the maximum number of children. The runtime of this
           operation scales with the number of nodes we need to visit, and we
           need to visit all the nodes in the tree.

           Memory usage: O(h), where h is the height of the calling BinaryTree
           object. This is because this method is recursive; and the amount of
           memory needed by the call stack as we traverse down the tree to a
           leaf, will depend on how many levels there are between the leaves
           and the root of the tree (the same goes for its nested subtrees).

           If the tree is balanced, then this runtime can also be expressed
           using O(log(n)).

        """
        # Traverse left subtree, if it exists
        if node is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
            visit(node.data)
        # Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
           Start at the given node and visit each node with the given function.

           Running time: O(n), where n is the number of nodes in the tree.
           This is under the conditions that the tree is balanced, where each
           node has the maximum number of children. The runtime of this
           operation scales with the number of nodes we need to visit, and we
           need to visit all the nodes in the tree.

           Memory usage: O(h), where h is the height of the calling BinaryTree
           object. This is because this method is iterative; and the amount of
           memory needed to perform all our iterations will depend on how many
           levels we need to traverse to get to the deepest leaf, from the root
           of the tree.

           If the tree is balanced, then this runtime can also be expressed
           using O(log(n)).

        """
        # TODO: Traverse in-order without using recursion (stretch challenge)
        to_vist = Stack()
        already_visited = list()
        # go down the left subtree
        while node.is_leaf() is False or node.left in already_visited:
            to_vist.push(node)
            node = node.left
        # visiting a node
        visit(node)
        already_visited.append(node)
        node = to_vist.pop()
        # going down the right subtree
        while node.is_leaf() is False or node.left in already_visited:
            to_vist.push(node)
            node = node.left

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
           Start at the given node and visit each node with the given function.

           Running time: O(n), where n is the number of nodes in the tree.
           This is under the conditions that the tree is balanced, where each
           node has the maximum number of children. The runtime of this
           operation scales with the number of nodes we need to visit, and we
           need to visit all the nodes in the tree.

           Memory usage: O(h), where h is the height of the calling BinaryTree
           object. This is because this method is recursive; and the amount of
           memory needed by the call stack as we traverse down the tree to a
           leaf, will depend on how many levels there are between the leaves
           and the root of the tree (the same goes for its nested subtrees).

           If the tree is balanced, then this runtime can also be expressed
           using O(log(n)).

        """
        if node is not None:
            # Visit this node's data with given function
            visit(node.data)
            # Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.left, visit)
            # Traverse right subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
           Start at the given node and visit each node with the given function.

          Running time: O(n), where n is the number of nodes in the tree.
          This is under the conditions that the tree is balanced, where each
          node has the maximum number of children. The runtime of this
          operation scales with the number of nodes we need to visit, and we
          need to visit all the nodes in the tree.

          Memory usage: O(h), where h is the height of the calling BinaryTree
          object. This is because this method is iterative; and the amount of
          memory needed to perform all our iterations will depend on how many
          levels we need to traverse to get to the deepest leaf, from the root
          of the tree.

          If the tree is balanced, then this runtime can also be expressed
          using O(log(n)).

       """
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
           Start at the given node and visit each node with the given function.

           Running time: O(n), where n is the number of nodes in the tree.
           This is under the conditions that the tree is balanced, where each
           node has the maximum number of children. The runtime of this
           operation scales with the number of nodes we need to visit, and we
           need to visit all the nodes in the tree.

           Memory usage: O(h), where h is the height of the calling BinaryTree
           object. This is because this method is recursive; and the amount of
           memory needed by the call stack as we traverse down the tree to a
           leaf, will depend on how many levels there are between the leaves
           and the root of the tree (the same goes for its nested subtrees).

           If the tree is balanced, then this runtime can also be expressed
           using O(log(n)).

      """
        if node is not None:
            # Traverse left subtree, if it exists
            self._traverse_post_order_recursive(node.left, visit)
            # Traverse right subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit)
            # Visit this node's data with given function
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
           Start at the given node and visit each node with the given function.

           Running time: O(n), where n is the number of nodes in the tree.
           This is under the conditions that the tree is balanced, where each
           node has the maximum number of children. The runtime of this
           operation scales with the number of nodes we need to visit, and we
           need to visit all the nodes in the tree.

           Memory usage: O(h), where h is the height of the calling BinaryTree
           object. This is because this method is iterative; and the amount of
           memory needed to perform all our iterations will depend on how many
           levels we need to traverse to get to the deepest leaf, from the root
           of the tree.

           If the tree is balanced, then this runtime can also be expressed
           using O(log(n)).

       """
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree.

        """
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal
           (BFS). Start at the given node and visit each node with the given
           function.

           Running time: O(n), where n is the number of nodes in the tree.
           This is under the conditions that the tree is balanced, where each
           node has the maximum number of children. The runtime of this
           operation scales with the number of nodes we need to visit, and we
           need to visit all the nodes in the tree.

           Memory usage: O(2^(h - 1), where h is the height of the tree. This
           is because the total amount of space needed by this method scales
           asymptotically with the memeory used up by the queue.

           Because the maximum number of nodes at any level in the tree scales
           with the powers of two (double the possible number of nodes at the
           previous level), we can say the queue space requirement scales on
           the magnitude of O(2^(h-1)). If the tree is balanced, then we can
           alternatively express this as O(n/2), because at the lowest level we
           need the most space for the queue, and the lowest level would
           contain half the nodes of the entire tree overall.

       """
        # Create queue to store nodes not yet traversed in level-order
        queue = Queue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.list.length() == 0:
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
