import unittest

from structures.array.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(2)

    def test_max_set(self):
        assert self.stack.max == 2

        self.stack.max = 10
        assert self.stack.max == 10

    def test_top_initialised(self):
        assert self.stack.top == -1

    def test_array_initialised(self):
        self.stack.max = 3
        expected_stack = [None, None, None]
        assert self.stack.array == expected_stack

    def test_push_on_stack(self):
        assert self.stack.push(0) == 0
        assert self.stack.push(1) == 0
        assert self.stack.array == [0, 1]

    def test_stack_is_full(self):
        assert not self.stack.is_full()
        for i in range(0, self.stack.max):
            assert self.stack.push(i) == 0
        assert self.stack.is_full()

    def test_pop_from_stack(self):
        assert self.stack.push(0) == 0
        assert self.stack.push(1) == 0

        assert self.stack.pop() == 0
        assert self.stack.array == [0, None]

        assert self.stack.pop() == 0
        assert self.stack.array == [None, None]

    def test_stack_is_empty(self):
        assert self.stack.is_empty()
        assert self.stack.push(1) == 0
        assert not self.stack.is_empty()

    def test_default_updates(self):
        self.default = 'X'
        self.stack.max = 5
        self.stack.default = self.default

        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        assert self.stack.array == [0, 1, 2, 'X', 'X']