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
