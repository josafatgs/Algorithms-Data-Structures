class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def AddNode(self, data):
        newNode = Node(data)
        current = self.head
        #We go to the last element of the linked list
        while current.next != None:
            current = current.next
        #Once we are on the last element of the linked list
        #we put the pointer to the new node
        current.next = newNode

    def Length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total
    def Display(self):
        elements= []
        current = self.head
        while current.next != None:
            current = current.next
            elements.append(current.data)
        print(elements)
    
    def Get(self,targetIndex):
        if targetIndex >= self.Length():
            print("Index out of range")
            return None
        index = 0
        current = self.head
        while True:
            current = current.next
            if index == targetIndex:
                return current.data
            index += 1
    def Delete(self,targetIndex):
        if targetIndex >= self.Length():
            print("Index out of range")
            return None
        index = 0
        current = self.head
        while True:
            previous = current
            current = current.next
            if index == targetIndex:
                previous.next = current.next
                return
            index += 1

            




myLinkedList = LinkedList()
myLinkedList.Display()
myLinkedList.AddNode(1)
myLinkedList.AddNode(2)
myLinkedList.AddNode(3)
myLinkedList.AddNode(4)
myLinkedList.Display()
print(myLinkedList.Get(0))
myLinkedList.Delete(0)
myLinkedList.Display()
