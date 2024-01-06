import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    def find_max_value(node):
        if node is None:
            return float("-inf")

        left_max_value = solution(node.left)
        right_max_value = solution(node.right)
        return max(left_max_value, node.value, right_max_value)

    return find_max_value(root)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
