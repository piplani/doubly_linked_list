class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            last = temp
            print temp.data,
            temp = temp.next
        print
        
        while last:
            print last.data,
            last = last.prev

if __name__ == '__main__':
    llist = DoublyLinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    second.prev = llist.head
    third.prev = second
    llist.printlist()
