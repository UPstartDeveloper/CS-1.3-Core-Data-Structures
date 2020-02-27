from set import Set
import unittest


class SetTests(unittest.TestCase):
    '''Unit tests for the Set class.'''
    def setUp(self):
        '''Run before each test to initialize commonly used variables.'''
        self.elements = [1, 2, 3]

    def test_init_no_elements(self):
        '''Test the Set constructor method, no elements passed in.'''
        set = Set()
        assert set.size == 0

    def test_init_with_elements(self):
        '''Test the Set constructor when elements are passed in.'''
        set = Set(self.elements)
        assert set.size == 3
        # test the values that got added to the collection
        assert set.collection.keys() == self.elements
        assert set.collection.values() == [None for i in range(set.size)]
        assert set.collection.get(1) is None
        assert set.collection.contains(1) is True
        assert set.collection.get(2) is None
        assert set.collection.contains(2) is True
        assert set.collection.get(3) is None
        assert set.collection.contains(3) is True

    def test_contains(self):
        '''Test the contains method of the Set class.'''
        # test with no elememts
        set = Set()
        assert set.contains(1) is False
        # test with elememts
        set = Set(self.elements)
        for element in self.elements:
            assert set.contains(element) is True

    def test_add(self):
        '''Test the add method of the Set class.'''
        # adding an item after instaniation, no inital elements
        set = Set()
        assert set.size == 0
        set.add(1)
        assert set.size == 1
        assert set.contains(1) is True
        # adding an item after instaniation, 3 inital elements
        set = Set(self.elements)
        assert set.size == 3
        set.add(4)
        assert set.size == 4
        assert set.contains(4) is True

    def test_remove(self):
        '''Test the remove method of the Set class.'''
        # test remove after instaniation, 3 initial elements
        set = Set(self.elements)
        size = set.size
        for element in self.elements:
            set.remove(element)
            size -= 1
            assert set.size == size
            assert set.contains(element) is False

    def test_union_one_empty_one_with_items(self):
        '''Test the union method of the Set class.'''
        set_one = Set()
        set_two = Set(self.elements)
        set_three = set_one.union(set_two)
        assert set_three.size == 3
        for element in self.elements:
            assert set_three.contains(element) is True

    def test_union_both_with_items_no_duplicates(self):
        '''Test the union method of the Set class.'''
        more_elements = [4, 5, 6]
        set_one = Set(more_elements)
        set_two = Set(self.elements)  # elements is [1, 2, 3]
        set_three = set_one.union(set_two)
        assert set_three.size == 6
        # init a list of the elements to check are in set_three
        all_elements = self.elements
        for element in more_elements:
            all_elements.append(element)
        # check if the appropiate elements are in set_three
        for element in all_elements:
            assert set_three.contains(element) is True

    def test_union_both_with_items_and_duplicates(self):
        '''Test the union method of the Set class.'''
        set_one = Set(self.elements)
        set_two = Set(self.elements)
        set_three = set_one.union(set_two)
        assert set_three.size == 3
        for element in self.elements:
            assert set_three.contains(element) is True
