#write a program to create a class/structure TreeNode to represent a node in a binary tree. Each node should have three 
# attributes: data, left and right. then create a class/structure Binary tree to represent the binary tree itslef.
# implement the following: 1. insert(data): Insert a new node with the given data into the binary tree (assume a simple insertion without balancing
# in_order_traversal(): Perform an in-order traversal of the binary tree and print the data of each node.) 
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def in_order_traversal(self):
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        if node is not None:
            self._in_order_recursive(node.left)
            print(node.data, end=" ")
            self._in_order_recursive(node.right)
# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)
    print("In-order Traversal:")
    tree.in_order_traversal()
