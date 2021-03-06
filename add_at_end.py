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
        # if you want to print in reverse order
        """
        while last:
            print last.data,
            last = last.prev
        """

    def append(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


if __name__ == '__main__':
    llist = DoublyLinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    second.prev = llist.head
    third.prev = second
    print "before adding"
    llist.printlist()
    llist.append(4)
    print "after adding"
    llist.printlist()
