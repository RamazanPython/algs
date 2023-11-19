import unittest

from task_d import solution


class Node:

    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class TestSolution(unittest.TestCase):

    def test_1(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)

        idx = solution(node0, "node2")
        assert idx == 2

    def test_2(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)

        idx = solution(node0, "node0")
        assert idx == 0

    def test_3(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)

        idx = solution(node0, "111111")
        assert idx == -1


if __name__ == '__main__':
    unittest.main()
