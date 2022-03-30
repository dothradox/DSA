import unittest
from merge_sort import mergeSort
from insertion_sort import insertion_sort


class TestSearch(unittest.TestCase):
    def test_merge(self):
        result = [1, 2, 3, 4, 5]
        sample2 = [5, 4, 3, 2, 1]
        sample3 = [4, 2, 3, 1, 5]
        self.assertListEqual(mergeSort(result), result)
        self.assertListEqual(mergeSort(sample2), result)
        self.assertListEqual(mergeSort(sample3), result)

    def test_insertion(self):
        result = [1, 2, 3, 4, 5]
        sample2 = [5, 4, 3, 2, 1]
        sample3 = [4, 2, 3, 1, 5]
        self.assertListEqual(insertion_sort(result), result)
        self.assertListEqual(insertion_sort(sample2), result)
        self.assertListEqual(insertion_sort(sample3), result)
