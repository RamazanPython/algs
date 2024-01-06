import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    stack = [[root, float("-inf"), float("inf")]]
    while stack:
        node, left, right = stack.pop()
        if node is None:
            continue

        if not (left < node.value < right):
            return False

        stack.append([node.left, left, node.value])
        stack.append([node.right, node.value, right])

    return True


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
