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

    # add a new node to the beginning of the list
    def prepend(self, data):
        # create a new node
        new_node = Node(data)

        # check if it is an empty list or not
        if not self.head:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    # add a new node after a given node
    def insert(self, prev_node_data, data):
        # create a new node
        new_node = Node(data)

        # transverse through the list to find prev_node_data
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next

        if not current:
            print(f"The node with data '{prev_node_data}' was not found.")
            return
        
        new_node.next = current.next
        current.next = new_node

    # remove a node from the list 
    def delete(self, key):
        # a node can be removed from the beginnign (head), end (tail), or middle (any other position)
        current = self.head

        # if the node to be removed is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        # if the node to be removed is not the head
        prev = None  # track the node before the one to be removed
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"No node was deleted. Node with data '{key}' was not found.")
            return
        
        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head

        # transverse the list till current.data and key matches
        while current and current.data != key:
            current = current.next
        
        if not current:
            print(f"No node was returned. Node with data '{key}' was not found.")
            return
        
        return True

    def printList(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")