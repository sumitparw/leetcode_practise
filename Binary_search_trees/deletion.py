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
def getminvalue(root):
    current = root
    while current.left is not None:
        current=current.left
    return current
def delete(root,key):
    if root is None:
        return None
    if root.key<key:
        root.right = delete(root.right,key)
    elif root.key>key:
        root.left = delete(root.left,key)
    else:
        if root.left is None:
            temp = root.right
            root= None
            return temp
        elif root.right is None:
            temp = root.right
            root= None
            return temp
        else:
            temp =getminvalue(root.right)
            root.key = temp.key
            root.right= delete(root.right,temp.key)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
root = Node(50)
insert(root, Node(30))
insert(root, Node(20))
insert(root, Node(40))
insert(root, Node(70))
insert(root, Node(60))
insert(root, Node(80))
#print(search(root,40))

# Print inoder traversal of the BST
inorder(root)

delete(root, 20)
print("Inorder traversal of the modified tree")
print(inorder(root))

