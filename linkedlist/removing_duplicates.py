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
    def remove_duplicate(self):
        s = set()
        temp = self.head
        while(temp):
            if temp.data not in s:
                s.add(temp.data)
                prev = temp
                temp = temp.next
            else:
                prev.next = temp.next
                temp = temp.next
                
if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_start(1)
    llist.append(3)
    llist.append(2)
    llist.append(3)
    llist.append(2)
    print("before")
    llist.printList()
    llist.remove_duplicate()

    print("after")
    llist.printList()



