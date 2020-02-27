from set import Set
import unittest


class SetTests(unittest.TestCase):
    '''Unit tests for the Set class.'''
    def test_init_no_elements(self):
        '''Test the Set constructor method, no elements passed in.'''
        set = Set()
        assert set.size == 0

    def test_init_with_elements(self):
        '''Test the Set constructor when elements are passed in.'''
        elements = [1, 2, 3]
        set = Set(elements)
        assert set.size == 3
        # test the values that got added to the collection
        assert set.collection.keys() == elements
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
        elements = [1, 2, 3]
        set = Set(elements)
        for element in elements:
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
        set = Set([1, 2, 3])
        assert set.size == 3
        set.add(4)
        assert set.size == 4
        assert set.contains(4) is True

    def test_remove(self):
        '''Test the remove method of the Set class.'''
        # test remove after instaniation, 3 initial elements
        elements = [1, 2, 3]
        set = Set(elements)
        size = set.size
        for element in elements:
            set.remove(element)
            size -= 1
            assert set.size == size
            assert set.contains(element) is False

    def test_union_one_empty_one_with_items(self):
        '''Test the union method of the Set class.'''
        elements = [1, 2, 3]
        set_one = Set()
        set_two = Set([1, 2, 3])
        set_three = set_one.union(set_two)
        assert set_three.size == 3
        for element in elements:
            assert set_three.contains(element) is True
