class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return f"Inserted '{data}' at the beginning."

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return f"Inserted '{data}' at the end."

    def remove_beginning(self):
        if not self.head:
            return "List is empty."
        removed_value = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return f"Removed '{removed_value}' from the beginning."

    def remove_end(self):
        if not self.head:
            return "List is empty."
        if self.head == self.tail:
            removed_value = self.head.data
            self.head = self.tail = None
            return f"Removed '{removed_value}' from the end."
        current = self.head
        while current.next != self.tail:
            current = current.next
        removed_value = self.tail.data
        current.next = None
        self.tail = current
        return f"Removed '{removed_value}' from the end."

    def remove_value(self, value):
        if not self.head:
            return "List is empty."

        if self.head.data == value:
            self.remove_beginning()
            return f"Removed node with value '{value}'."

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next:
            removed_value = current.next.data
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            return f"Removed node with value '{removed_value}'."
        else:
            return f"'{value}' not found in the list."

    def search(self, value):
        if not self.head:
            return "List is empty."
        current = self.head
        position = 1
        while current:
            if current.data == value:
                return f"'{value}' found at position {position}."
            current = current.next
            position += 1
        return f"'{value}' not found in the list."

    def display(self):
        if not self.head:
            return "List is empty."
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " → ".join(result)
