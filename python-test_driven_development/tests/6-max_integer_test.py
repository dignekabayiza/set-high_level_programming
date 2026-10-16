#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max at the end of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max inside an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Max in the middle of the list."""
        self.assertEqual(max_integer([1, 5, 2]), 5)

    def test_one_element(self):
        """List with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Default argument returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """List of only negative numbers."""
        self.assertEqual(max_integer([-5, -1, -9]), -1)

    def test_mixed_signs(self):
        """List with negative, zero and positive numbers."""
        self.assertEqual(max_integer([-3, 0, 3]), 3)

    def test_duplicates(self):
        """List where all elements are equal."""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_big_integers(self):
        """Very large integers."""
        self.assertEqual(max_integer([10 ** 20, 10 ** 19]), 10 ** 20)

    def test_floats(self):
        """List of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        """List mixing integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_infinity(self):
        """List containing infinity."""
        self.assertEqual(max_integer([1, float('inf')]), float('inf'))

    def test_list_of_strings(self):
        """List of strings compares alphabetically."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_string_argument(self):
        """A string is treated as a sequence of characters."""
        self.assertEqual(max_integer("hello"), "o")

    def test_tuple_argument(self):
        """A tuple works like a list."""
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_list_of_lists(self):
        """List of lists compares element by element."""
        self.assertEqual(max_integer([[1, 2], [3]]), [3])

    def test_none_argument(self):
        """None raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_integer_argument(self):
        """An integer raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_mixed_types(self):
        """Uncomparable elements raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])
        with self.assertRaises(TypeError):
            max_integer(["a", 1])

    def test_too_many_arguments(self):
        """Two arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1], [2])


if __name__ == '__main__':
    unittest.main()
