from set import Set
import unittest


class SetTests(unittest.TestCase):
    '''Unit tests for the Set class.'''
    def test_init(self):
        '''Test the Set constructor method.'''
        set = Set()
        assert set.size == 0
