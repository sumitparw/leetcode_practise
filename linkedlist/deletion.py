class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def add_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node =Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def display(self):
        current = self.head
        while(current != None):
            print(current.data, end=' ')
            current = current.next



llist = LinkedList()
n = 5
lists = [204,105,110,112,114]
for i in range(n):
    llist.append(lists[i])
print("Linked list data: ", end=' ')
llist.display()

# k = 0
# while k!=1:
#     inp = input("\n do you want to enter more:")
#     if(inp == 'n'):
#         k = 1
#         continue
#     else:
#         inp = int(input("enter element to linked list at start(0) or end(1) or after(2):"))
#         if inp == 0:
#             inp = input("enter element to linked list at start:")
#             llist.add_start(inp)
#         if inp == 1:
#             inp = input("enter element to linked list at end:")
#             llist.append(inp)
#         else:
#             prev = int(input("enter element to linked list after node:"))
#             data = input("enter element to linked list:")
#             llist.insert_after(llist.head.next,data)
# print("Linked list data after entering more : ", end=' ')
# llist.display()
#
#






