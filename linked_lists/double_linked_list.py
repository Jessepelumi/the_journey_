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

    # insert a node after a given node
    def insert(self, prev_node_data, data):
        # create a new node
        new_node =  Node(data)

        # find the node 
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next

        if not current:
            print(f"No node was found. Node with data '{prev_node_data}' was not found.")
            return
        
        next_node = current.next
        if not next_node:
            current.next = new_node
            new_node.prev = current
            return

        new_node.next = next_node
        next_node.prev = new_node
        current.next = new_node
        new_node.prev = current

    # remove a node from the list
    def delete(self, key):
        # make sure the list is not empty 
        # remove head node 
        # remove other nodes 
        current = self.head

        if current and current.next == key:
            self.head = current.next
            self.head.prev = None
            current = None
            return

