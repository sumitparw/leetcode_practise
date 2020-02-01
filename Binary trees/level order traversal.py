
#o(n) approaach
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



def printLevelOrder(root):
    if root is None:
        return
    q=[]
    q.append(root)
    while len(q):
        print(q[0].key)
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
# Driver code
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level Order Traversal of binary tree is -",printLevelOrder(root))