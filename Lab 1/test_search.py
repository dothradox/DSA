import unittest
from search import binary_search, linear_search


class TestSearch(unittest.TestCase):
    def test_binary(self):
        sample = [41, 5, 33, 38, 19, 40, 28, 9, 22, 35]
        assert linear_search(sample, 40) == 5
        assert linear_search(sample, 100) == -1

    def test_linear(self):
        sample = [5, 9, 19, 22, 28, 33, 35, 38, 40, 41]
        assert binary_search(sample, 35) == 6
        assert binary_search(sample, 100) == -1

    # def test_binary(self):
    #     sample = [41, 5, 33, 38, 19, 40, 28, 9, 22, 35]
    #     assert linear_search(sample, 40) == 5
    #     assert linear_search(sample, 100) == -1

    # def test_linear(self):
    #     sample = [5, 9, 19, 22, 28, 33, 35, 38, 40, 41]
    #     assert binary_search(sample, 35) == 6
    #     assert binary_search(sample, 100) == -1
