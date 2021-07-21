class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            return 
    
        temp = self.head
        while(temp.next):
            temp=temp.next
        new = Node(data)
        temp.next = new
    
    # insert at front
    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, val):
        temp = self.head
        prev = self.head
        if(self.head.val == val and self.head.next):
            self.head = self.head.next
            return 
        while(temp.val != val):
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp.next = None
        del temp
        

    def search(self, key):
        current = self.head
        while current is not None:
            if current.val == key:
                return True
            current = current.next
        return False
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.val,end=" ")
            temp=temp.next
        

linklist = LinkedList()
linklist.insert(5)
linklist.insert(3)
linklist.insert(2)
linklist.insert(1)

linklist.delete(2)

linklist.delete(1)
linklist.insert(9)
linklist.insert(10)
linklist.insert(11)
linklist.printlist()


        