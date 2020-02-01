class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.key = data
def inorder(temp):
    if(not temp):
        return
    inorder(temp.left)
    print(temp.key,end= " ")
    inorder(temp.right)
def deepextnode(root,d_node):
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp == d_node:
            temp = None
            return
        if temp.left:
            if temp.left == d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
        if temp.right:
            if temp.right == d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)





def deletion(root, key):
    q = []
    q.append(root)
    key_node = None
    while len(q):
        temp = q.pop(0)
        if temp.key == key:
            key_node =temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x= temp.key
        deepextnode(root,temp)
        key_node.key = x
    return root

# Driver code
if __name__ == '__main__':

    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    inorder(root)
    key = 11
    root = deletion(root, key)
    print()
    print("The tree after the deletion;")
    inorder(root)
