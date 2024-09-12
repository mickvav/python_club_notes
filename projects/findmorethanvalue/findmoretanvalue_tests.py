#!/usr/bin/env python3

import unittest
from findmorethanvalue import findmorethanvalue


class TestFindMoreThanValue(unittest.TestCase):

    def testemptylist(self):
        self.assertEqual(findmorethanvalue([], 5), [])

    def test_no_elements_greater_than_value(self):
        self.assertEqual(findmorethanvalue([1, 2, 33], 55), [])

    def test_some_elements_greater_than_value(self):
        self.assertEqual(findmorethanvalue([1, 2, 3, 6, 77], 5), [6, 77])

if __name__ == '__main__':
    unittest.main()