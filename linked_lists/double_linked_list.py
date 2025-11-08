# Doubly linked list implementation 

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # add a new node to the end of the list
    def append(self, data):
        # create a new node 
        new_node = Node(data)

        # check if the head exist (if the list is empty or not)
        if not self.head:
            self.head = new_node
            return
        
        # head exists 
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node  # append new node to the list
        new_node.prev = last  # set prev of new node to the last node 

    # add a new node to the beginning of the list  
    def prepend(self, data):
        # create a new node
        new_node = Node(data)

        # check if the head exists 
        if not self.head:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

