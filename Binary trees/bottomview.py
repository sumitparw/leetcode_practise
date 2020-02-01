class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive function pritn left view of a binary tree
def bottomViewUtil(root):
    # Base Case
    if root is None:
        return
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.left is None and temp.right is None:
            print(temp.data)
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)



# Driver program to test above function
root = Node(12)
root.left = Node(10)
root.left.left = Node(50)
root.left.right = Node(55)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)

bottomViewUtil(root)