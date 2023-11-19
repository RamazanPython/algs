import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def get_by_index(node, idx: int):
    while idx and node:
        node = node.next_item
        idx -= 1

    return node


def solution(node, idx: int):
    if idx == 0:
        next_node = node.next_item
        node.next_item = None
        return next_node

    previous_node = get_by_index(node, idx - 1)
    next_node = previous_node.next_item
    previous_node.next_item = next_node.next_item
    return node


def print_linked_list(node):
    while node:
        print(node.value, end=' -> ')
        node = node.next_item
    print(None)


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
