# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 17:00
# @Author  : JacobZhou
# @Email   : JacobZhou@canway.net
# @File    : tests.py
# @Project : AlgorithmInterview
import unittest

from LearnDataStructureAlgorithm.Search import linear_search, intpolsearch
from LearnDataStructureAlgorithm.Sort import bubble_sort, insertion_sort, selection_sort


class LearnTest(unittest.TestCase):
    def tearDown(self) -> None:
        """
        每个测试用例运行之后执行
        :return:
        """
        pass

    def setUp(self) -> None:
        """
        每个测试用例运行之前执行
        :return:
        """
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        """
        必须使用@classmethod装饰器，所有测试用例运行完成后运行一次
        :return:
        """
        pass

    @classmethod
    def setUpClass(cls) -> None:
        """
        必须使用@classmethod装饰器，所有测试用例运行钱运行一次
        :return:
        """
        pass

    def test_linear_search(self):
        l = [64, 34, 25, 12, 22, 11, 90]
        rst = linear_search(l, 12)
        self.assertTrue(rst)

    def test_intpolsearch(self):
        l = [2, 6, 11, 19, 27, 31, 45, 121]
        rst = intpolsearch(l, 2)
        self.assertEqual(rst, "Found 2 at index 0")

    def test_bubble_sort(self):
        l = [19, 2, 31, 45, 6, 11, 121, 27]
        rst = bubble_sort(l)
        self.assertEqual(rst, [2, 6, 11, 19, 27, 31, 45, 121])

    def test_insertion_sort(self):
        l = [19, 2, 31, 45, 6, 11, 121, 27]
        rst = insertion_sort(l)
        self.assertEqual(rst, [2, 6, 11, 19, 27, 31, 45, 121])

    def test_selection_sort(self):
        l = [19, 2, 31, 45, 6, 11, 121, 27]
        rst = selection_sort(l)
        self.assertEqual(rst, [2, 6, 11, 19, 27, 31, 45, 121])


if __name__ == '__main__':
    unittest.main()
