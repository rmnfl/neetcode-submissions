class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key, val)

        if not self.root:
            self.root = TreeNode(key, val)
            return

        curr = self.root

        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = node
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = node
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        if not self.root:
            return -1

        curr = self.root

        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        
        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1

        curr = self.root

        while curr.left:
            curr = curr.left

        return curr.val


    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root

        while curr.right:
            curr = curr.right

        return curr.val

    def remove(self, key: int) -> None:

        def deleteNode(root, key):
            if not root:
                return None

            if key < root.key:
                root.left = deleteNode(root.left, key)
            elif key > root.key:
                root.right = deleteNode(root.right, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                
                minNode = self._getMinNode(root.right)
                root.key = minNode.key
                root.val = minNode.val

                root.right = deleteNode(root.right, minNode.key)

            return root

        self.root = deleteNode(self.root, key)


    def getInorderKeys(self) -> List[int]:
        result = []
        
        def dfs(root):
            nonlocal result
            if not root:
                return

            dfs(root.left)
            result.append(root.key)
            dfs(root.right)

        dfs(self.root)
        return result
    

    def _getMinNode(self, root):
        curr = root

        while curr and curr.left:
            curr = curr.left

        return curr