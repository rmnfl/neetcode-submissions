class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class TreeMap:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key, val)

        if self.root is None:
            self.root = node
            return

        curr = self.root

        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = node
                    return

                curr = curr.left

            elif key > curr.key:
                if curr.right is None:
                    curr.right = node
                    return

                curr = curr.right

            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root

        while curr is not None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val

        return -1

    def getMin(self) -> int:
        min_node = self._findMinNode(self.root)
        return min_node.val if min_node is not None else -1

    def getMax(self) -> int:
        if self.root is None:
            return -1

        curr = self.root

        while curr.right is not None:
            curr = curr.right

        return curr.val

    def remove(self, key: int) -> None:
        self.root = self._removeHelper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        result = []
        self._inorderTraversal(self.root, result)
        return result

    def _findMinNode(self, root):
        curr = root

        while curr is not None and curr.left is not None:
            curr = curr.left

        return curr

    def _removeHelper(self, root, key):
        if root is None:
            return None

        if key < root.key:
            root.left = self._removeHelper(root.left, key)
        elif key > root.key:
            root.right = self._removeHelper(root.right, key)
        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            successor = self._findMinNode(root.right)
            root.key = successor.key
            root.val = successor.val
            root.right = self._removeHelper(root.right, successor.key)

        return root

    def _inorderTraversal(self, root, result):
        if root is None:
            return

        self._inorderTraversal(root.left, result)
        result.append(root.key)
        self._inorderTraversal(root.right, result)
