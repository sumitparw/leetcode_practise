class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.key = data
def printInorder(temp):
    if temp:
        printInorder(temp.left)
        print(temp.key),
        printInorder(temp.right)
def printPreorder(temp):
    if temp:
        print(temp.key),
        printPreorder(temp.left)
        printPreorder(temp.right)
def printPostorder(temp):
    if temp :
        printPostorder(temp.left)
        printPostorder(temp.right)
        print(temp.key),
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Preorder traversal of binary tree is",printPreorder(root))

    print("\nInorder traversal of binary tree is",printInorder(root))

    print("\nPostorder traversal of binary tree is",printPostorder(root))