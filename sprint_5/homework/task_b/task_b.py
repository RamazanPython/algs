import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def get_height(root):
    if root is None:
        return 0

    left_height = 1 + get_height(root.left)
    right_height = 1 + get_height(root.right)
    return max(left_height, right_height)


def solution(root) -> bool:
    if root is None:
        return True

    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return abs(left_height - right_height) <= 1 and solution(root.left) and solution(root.right)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
