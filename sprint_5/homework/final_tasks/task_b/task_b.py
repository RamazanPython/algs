# ID - 104293198
# Time - O(logN)
# Space - O(1)

"""
Принцип работы

Первым делом я ищу вершину по значению, которую нужно удалить. Тут все просто. Если корень больше искомого значения,
ищем слева, иначе справа.

Далее когда мы находим нужную вершину и делаем оптимизацию. Если у удаляемой вершины только одни потомки, то возвращаем
их. Иначе мы ищем самый маленький элемент в правом поддереве. Это самый левый элемент справа. Для оптимизации сохраняем
его и его родителя, чтобы дважды не пробегаться по дереву. Когда мы находим самый маленький элемент справа и делаем его
корнем, а у его родителя удалеяем ссылку.
"""

import os

from typing import Optional

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def remove(root, key) -> Optional[Node]:
    if root is None:
        return

    if root.value > key:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        min_right = root.right
        min_right_parent = root
        while min_right.left:
            min_right_parent = min_right
            min_right = min_right.left

        root.value = min_right.value

        if min_right_parent.right == min_right:
            min_right_parent.right = min_right.right
        else:
            min_right_parent.left = min_right.right

    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()
