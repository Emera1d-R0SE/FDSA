class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        
        last.next = new_node  # Link the last node to the new node

    def delete_node(self, data):
        current = self.head
        if current and current.data == data:  # If the node to delete is the head
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != data:  # Find the node to delete
            prev = current
            current = current.next

        if current is None:  # Node with the data doesn't exist
            return

        prev.next = current.next  # Bypass the current node
        current = None  # Delete the node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

# Test the linked list operations
linked_list = LinkedList()

# Insert elements at the beginning
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
print("Linked list after inserting 20, 10 at the beginning:")
linked_list.traverse()

# Insert elements at the end
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)
print("\nLinked list after inserting 30, 40 at the end:")
linked_list.traverse()

# Delete a node
linked_list.delete_node(20)
print("\nLinked list after deleting node with data 20:")
linked_list.traverse()

# Traverse the list
print("\nTraversing the linked list:")
linked_list.traverse()

