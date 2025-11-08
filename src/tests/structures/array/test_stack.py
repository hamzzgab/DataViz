import unittest

from structures.array.stack import Stack


class TestStack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stack = Stack()

    def test_max_set(self):
        assert self.stack.max == 5

        self.stack.max = 10
        assert self.stack.max == 10

    def test_top_initialised(self):
        assert self.stack.top == -1

    def test_array_initialised(self):
        self.stack.max = 5
        expected_stack = [None, None, None, None]
        assert self.stack.array == expected_stack
