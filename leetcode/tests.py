import unittest

from ArrayAndLinkedList.reverse_linked_list import ListNode, Solution


class AlgorithmInterviewTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('22222')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('4444444')

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('33333')

    def test_a_run(self):
        print('hello')
        self.assertEqual(1, 1)  # 测试用例

    def test_b_run(self):
        print('world')
        self.assertEqual(2, 2)  # 测试用例

    def test_reverse_linked_list(self):
        node5 = ListNode(5)
        node4 = ListNode(4, next=node5)
        node3 = ListNode(3, next=node4)
        node2 = ListNode(2, next=node3)
        node1 = ListNode(1, next=node2)
        curval = node1
        while curval:
            print(curval.val)
            curval = curval.next
        solution = Solution()
        head = solution.reverseList(node1)
        while head:
            print(head.val)
            head = head.next


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
