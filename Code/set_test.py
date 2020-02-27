from set import Set
import unittest


class SetTests(unittest.TestCase):
    '''Unit tests for the Set class.'''
    def setUp(self):
        '''Run before each test to initialize commonly used variables.'''
        self.elements = [1, 2, 3]
        self.more_elements = [4, 5, 6]

    def test_init_no_elements(self):
        '''Test the Set.__init__ method, no elements passed in.'''
        set = Set()
        assert set.size == 0

    def test_init_with_elements(self):
        '''Test the Set.__init__ when elements are passed in.'''
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
        '''Test the Set.contains method.'''
        # test with no elememts
        set = Set()
        assert set.contains(1) is False
        # test with elememts
        set = Set(self.elements)
        for element in self.elements:
            assert set.contains(element) is True

    def test_add(self):
        '''Test the Set.add method.'''
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
        '''Test the Set.remove method.'''
        # test remove after instaniation, 3 initial elements
        set = Set(self.elements)
        size = set.size
        for element in self.elements:
            set.remove(element)
            size -= 1
            assert set.size == size
            assert set.contains(element) is False

    def test_union_one_empty_one_with_items(self):
        '''Test the Set.union method.'''
        set_one = Set()
        set_two = Set(self.elements)
        set_three = set_one.union(set_two)
        assert set_three.size == 3
        for element in self.elements:
            assert set_three.contains(element) is True

    def test_union_both_with_items_no_duplicates(self):
        '''Test the Set.union method.'''
        set_one = Set(self.more_elements)
        set_two = Set(self.elements)  # elements is [1, 2, 3]
        set_three = set_one.union(set_two)
        assert set_three.size == 6
        # init a list of the elements to check are in set_three
        all_elements = self.elements
        for element in self.more_elements:
            all_elements.append(element)
        # check if the appropiate elements are in set_three
        for element in all_elements:
            assert set_three.contains(element) is True

    def test_union_both_with_items_and_duplicates(self):
        '''Test the Set.union method.'''
        set_one = Set(self.elements)
        set_two = Set(self.elements)
        set_three = set_one.union(set_two)
        assert set_three.size == 3
        for element in self.elements:
            assert set_three.contains(element) is True

    def test_intersection_all_unique_elements(self):
        '''Test the Set.intersection method.'''
        set_one = Set(self.elements)
        set_two = Set(self.more_elements)
        set_three = set_one.intersection(set_two)
        assert set_three.size == 0
        set_four = set_two.intersection(set_one)
        assert set_four.size == 0

    def test_intersection_different_set_sizes_all_unique_elements(self):
        '''Test the Set.intersection method.'''
        set_one = Set(self.elements)
        set_two = Set([7, 8, 9, 10])
        set_three = set_one.intersection(set_two)
        assert set_three.size == 0
        # test the output is same regardless of order
        set_four = set_two.intersection(set_one)
        print(set_four.collection.keys())
        assert set_four.size == 0

    def test_intersection_all_duplicates(self):
        '''Test the Set.intersection method.'''
        set_one = Set(self.elements)
        set_two = Set(self.elements)
        set_three = set_one.intersection(set_two)
        assert set_three.size == 3

    def test_intersection_duplicates_different_sizes(self):
        '''Test the Set.intersection method.'''
        set_one = Set(self.elements)
        set_two = Set([1, 2, 3, 4])
        set_three = set_one.intersection(set_two)
        # test size of the new set
        assert set_three.size == 3
        # test the wrong values are not in the set
        assert set_three.contains(4) is False
        # test the right values are in the set
        assert set_three.contains(1) is True
        assert set_three.contains(2) is True
        assert set_three.contains(3) is True
        # test that order doesn't matter
        set_three = set_two.intersection(set_one)
        assert set_three.size == 3
        assert set_three.contains(1) is True
        assert set_three.contains(2) is True
        assert set_three.contains(3) is True

    def test_intersection_duplicates_pull_from_both(self):
        '''Test the Set.intersection method.'''
        # only shared elements are 2, 3
        set_one = Set(self.elements)
        set_two = Set([2, 3, 4])
        set_three = set_one.intersection(set_two)
        # test size of the new set
        assert set_three.size == 2
        # test the wrong values are not in the set
        assert set_three.contains(4) is False
        assert set_three.contains(1) is False
        # test the right values are in the set
        assert set_three.contains(2) is True
        assert set_three.contains(3) is True
        # test that order doesn't matter
        set_three = set_two.intersection(set_one)
        assert set_three.size == 2
        assert set_three.contains(4) is False
        assert set_three.contains(1) is False
        assert set_three.contains(2) is True
        assert set_three.contains(3) is True
