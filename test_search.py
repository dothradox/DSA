import unittest
from search import binary_search


class TestSearch(unittest.TestCase):
    def test_equal(self):
        sorted_list = list(range(0, 100000))
        self.assertEqual(binary_search(sorted_list, 0, len(sorted_list), 711), 711)
        self.assertNotEqual(binary_search(sorted_list, 0, len(sorted_list), 711), 710)
        self.assertEqual(binary_search(sorted_list, 0, len(sorted_list), -5), -1)
