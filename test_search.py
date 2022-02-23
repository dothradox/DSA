import unittest
import random
from search import *


class TestSearch(unittest.TestCase):
    def test_equal(self):
        sorted_list = list(range(0, 1000000000))
        self.assertEqual(binary_search(random_list, 0, len(random_list), 711), 711)
        self.assertEqual(binary_search(random_list, 0, len(random_list), 711), 711)
