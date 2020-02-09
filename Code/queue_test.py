#!python

from queue import Queue
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        q = Queue()
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = Queue(['A', 'B', 'C'])
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length(self):
        q = Queue()
        assert q.length() == 0
        q.enqueue('A')
        assert q.length() == 1
        q.enqueue('B')
        assert q.length() == 2
        q.dequeue()
        assert q.length() == 1
        q.dequeue()
        assert q.length() == 0

    def test_enqueue(self):
        q = Queue()
        q.enqueue('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.enqueue('B')
        assert q.front() == 'A'
        assert q.length() == 2
        q.enqueue('C')
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_front(self):
        q = Queue()
        assert q.front() is None
        q.enqueue('A')
        assert q.front() == 'A'
        q.enqueue('B')
        assert q.front() == 'A'
        q.dequeue()
        assert q.front() == 'B'
        q.dequeue()
        assert q.front() is None

    def test_dequeue(self):
        q = Queue(['A', 'B', 'C'])
        assert q.dequeue() == 'A'
        assert q.length() == 2
        assert q.dequeue() == 'B'
        assert q.length() == 1
        assert q.dequeue() == 'C'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.dequeue()


class DequeTest(unittest.TestCase):
    def test_push_front(self):
        '''The deque is able to enqueue at the front of the list.'''
        d = Queue()
        assert d.is_empty() is True
        d.push_front('A')
        assert d.list[0] == 'A'
        d.push_front("B")
        assert d.list[0] == 'B'

    def test_push_back(self):
        '''The deque is able to enqueue at the back of the list.'''
        d = Queue()
        assert d.is_empty() is True
        d.push_back('A')
        assert d.list[0] == 'A'
        d.push_back("B")
        assert d.list[0] == 'A'
        assert d.list[1] == 'B'

    def test_back(self):
        '''The deque is able to shows last item without removing it.'''
        pass

    def test_pop_front(self):
        '''The deque is able to dequeue from the front.'''
        pass

    def test_pop_back(self):
        '''The deque is able to dequeue from back.'''
        pass


if __name__ == '__main__':
    unittest.main()
