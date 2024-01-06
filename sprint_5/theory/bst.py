class BinaryNode:

    def __init__(self, value: int) -> None:
        self.right = None
        self.left = None
        self.value = value


class BinaryTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: int) -> BinaryNode:
        if node is None:
            return BinaryNode(value=value)

        if node.value >= value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return node

    def __contains__(self, value):
        node = self.root
        while node:
            if node.value == value:
                return True

            if node.value > value:
                node = node.left
            else:
                node = node.right

        return False

    def remove(self, value: int):
        self.root = self._remove(self.root, value)

    def _remove_min(self, node: BinaryNode):
        if node.left is None:
            return node.right

        node.left = self._remove_min(node)
        return node

    def _remove(self, node: BinaryNode, value: int):
        if node is None:
            return

        if node.value > value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            original, node = node, node.right
            while node.left:
                node = node.left

            node.right = self._remove_min(original.right)
            node.left = original.left

        return node
