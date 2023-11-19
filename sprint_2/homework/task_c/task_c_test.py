import unittest

from task_c import get_by_index, solution, print_linked_list


class Node:

    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class TestGetByIndex(unittest.TestCase):

    def test_1(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)

        self.assertEqual(get_by_index(node0, 2), node2)

    def test_2(self):
        self.assertEqual(get_by_index(None, 2), None)

    def test_3(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)

        self.assertEqual(get_by_index(node0, 3), node3)


class TestSolution(unittest.TestCase):

    def test_1(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)

        head = solution(node0, 2)
        assert head.next_item.next_item is node3

    def test_2(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)

        head = solution(node0, 3)
        assert head.next_item.next_item.next_item is None

    def test_3(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)

        head = solution(node0, 0)
        assert head is node1

    def test_4(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)

        head = solution(node0, 1)
        assert head.next_item is node2


if __name__ == '__main__':
    unittest.main()
