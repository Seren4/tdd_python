import unittest

from errors import UnderflowException

from distlib.database import new_dist_class

from stack import Stack

class StackTest(unittest.TestCase):
    # todo check setup
    # todo parametrized test
    # todo renaming raccourci
    @classmethod
    def setUp(self):
        self.new_stack = Stack()

    @classmethod
    def tearDown(self):
        self.new_stack = None

    def test_should_be_empty_upon_creation(self):
        self.assertTrue(self.new_stack.is_empty())

    def test_size_should_be_zero_upon_creation(self):
        self.assertEqual(self.new_stack.get_size(), 0)

    def test_should_not_be_empty_after_one_push(self):
        self.new_stack.push(4)
        self.assertFalse(self.new_stack.is_empty())

    def test_size_should_be_two_after_two_pushes(self):
        self.new_stack.push(4)
        self.new_stack.push(5)
        self.assertEqual(self.new_stack.get_size(), 2)

    def test_should_throw_underflow_exception_on_pop_on_empty(self):
        with self.assertRaises(UnderflowException):
            self.new_stack.pop()

    def test_should_return_last_pushed_element_on_pop(self):
        element = 2
        self.new_stack.push(element)
        self.assertEqual(self.new_stack.pop(), element)

    def test_should_return_last_pushed_element_on_double_pop(self):
        self.new_stack.push(2)
        self.new_stack.push(4)
        self.assertEqual(self.new_stack.pop(), 4)

    def test_size_should_be_one_on_double_pushes_and_one_pop(self):
        self.new_stack.push(2)
        self.new_stack.push(4)
        result = self.new_stack.pop()
        self.assertEqual(result, 4)
        self.assertEqual(self.new_stack.get_size(), 1)

    def test_should_return_value_of_first_pushed_element_on_double_push_and_pop(self):
        self.new_stack.push(2)
        self.new_stack.push(4)
        self.new_stack.pop()
        result = self.new_stack.pop()
        self.assertEqual(result, 2)

    def test_should_return_last_pushed_element(self):
        self.new_stack.push(2)
        self.assertEqual(self.new_stack.peek(), 2)
        self.assertEqual(self.new_stack.get_size(), 1)










