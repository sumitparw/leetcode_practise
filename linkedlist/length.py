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
    def count_len(self):
        count = 0
        current = self.head
        while(current):
            count+=1
            current = current.next
        return count

    def recur_count_len(self, node):
        if not node:
            return 0
        else:
            return 1 + self.recur_count_len(node.next)
    def rec_len(self):
        return self.recur_count_len(self.head)

if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.insert_start(5)
    #llist.append(8)
    print(llist.rec_len())
    print("Linked List")
    llist.printList()



