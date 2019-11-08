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

    def insert_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def insert_after(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def loop(self):
        temp = self.head
        s = set()
        while(temp):
            if temp in s:
                return True
            else:
                s.add(temp)
            temp = temp.next
        return False
    def CreateLoop(self,index):
        temp = self.head
        for i in range(1,index):
            temp = temp.next
        end = self.head
        while(end.next):
            end = end.next
        end.next = temp
    def detectloop(self):
        if self.head is None:
            return
        slow = self.head
        fast = self.head
        flag = 0
        while(slow and slow.next and fast and fast.next and fast.next.next):
            if slow == fast and flag !=0:

                slow = slow.next
                count = 1
                while(slow != fast):
                    slow = slow.next
                    count += 1
                return count
            slow = slow.next
            fast = fast.next.next
            flag = 1
        return 0


if __name__ == "__main__":
    myLL = LinkedList()
    myLL.insert_start(1)
    myLL.append(2)
    myLL.append(3)
    myLL.append(4)
    myLL.append(5)
    #myLL.printList()
    myLL.CreateLoop(2)
    print(myLL.detectloop())



