class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    def insert_start(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head =new_node
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head= new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    def insert_after(self,prev_node,new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.insert_start(5)
    llist.append(8)
   
    llist.printList()



