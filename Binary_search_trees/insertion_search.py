class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.key = data
def insert(r,node):
    if r is None:
        r =node
    else:
        if r.key<node.key:
            if r.right is None:
                r.right =node
            else:
                insert(r.right,node)
        else:
            if r.left is None:
                r.left = node
            else:
                insert(r.left,node)
def search(root,key):
    if root is None or root.key == key:
        return root
    if root.key<key:
        return search(root.right,key)
    else:
        return search(root.left, key)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))
print(search(r,40))

# Print inoder traversal of the BST
inorder(r)