#Write a program to create a class/structure Node to represent a node in a singly linked list.
#Implement the following operation:
#1. append_node(data): appends node at the end
#2. search_node(data): search for a node with a particular value
#3. display_list(): prints the list


class Node:
    def __init__(self, data=None):
        self.data, self.next = data, None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def search_node(self, data):
        current = self.head  # Start from the head of the list
        while current != None:  # Traversal here
            if current.data == data:  # Check if the current node's data matches
                return True  # Data found
            current = current.next 
        return False

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
linked_list = SinglyLinkedList()
linked_list.append_node(10)
linked_list.append_node(20)
linked_list.append_node(30)
linked_list.display_list()

print(f"Searching for 20: {'Found' if linked_list.search_node(20) else 'Not Found'}")
print(f"Searching for 40: {'Found' if linked_list.search_node(40) else 'Not Found'}")

