class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
