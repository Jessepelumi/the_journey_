# Singly linked list implementation

"""
For a singly linked list, the list can only be transversed from left to right.
The Node class defines the structure of the nodes, having two components: the data and the reference to the next node in the sequence.
The head node is the starting point, the first node in the list. The node pointing to null is the tails node and signifies the end of the list.
The SinglyLinkedList class defines the linked list with all the available nodes linked together. 
"""

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # Initial value is None because other nodes do not exist yet.

# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None # Initially None because the list is empty

    # add a new node to the end of the list
    def append(self, data):
        # create a new node
        new_node = Node(data)

        # check if the head node exists
        if not self.head:
            self.head = new_node
            return

        # obtain the last node in the list
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def prepend(data):
        pass

    def insert(data):
        pass

    def delete(data):
        pass

    def search(data):
        pass

    def printList():
        pass