class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=' ')
            self.inorder_traversal(root.right)

# Usage
bst = BinarySearchTree()
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = bst.insert(root, key)

print("Inorder Traversal of the constructed BST:")
bst.inorder_traversal(root)

print("\nDelete 20")
root = bst.delete(root, 20)
print("Inorder Traversal after deletion:")
bst.inorder_traversal(root)
