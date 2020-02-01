class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.random = None


def deepcopy(head):
    if head is None:
        return
    current = head
    while current!=None:
        new =Node(current.val)
        new.next = current.next
        current.next=new
        current = new.next

    curr = head
    while curr != None:
        curr.next.random = curr.random.next
        curr = curr.next.next
    current =head
    dup_nonde =current.next
    while current.next !=None:
        temp =current.next
        current.next = current.next.next
        current =temp
    return dup_nonde
def printlist(root):
    current =root
    while current != None:
        print('data=',current.val,',','random=',current.random.val)
        current=current.next

original_list = Node(28)
original_list.next = Node(23)
original_list.next.next = Node(28)
original_list.next.next.next = Node(13)

original_list.random = original_list.next
original_list.next.random = original_list.next.next
original_list.next.next.random = original_list.next.next.next
original_list.next.next.next.random = original_list

cloned_list = deepcopy(original_list)
printlist(cloned_list)
