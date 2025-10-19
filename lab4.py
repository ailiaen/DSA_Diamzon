class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_beginning(self):
        if self.head is None:
            return None
        deleted_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return deleted_data

    def remove_at_end(self):
        if self.tail is None:
            return None
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            self.tail = None
            return deleted_data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_data = current.next.data
        current.next = None
        self.tail = current
        return deleted_data

    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            deleted_data = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return deleted_data
        current = self.head
        while current.next:
            if current.next.data == data:
                deleted_data = current.next.data
                current.next = current.next.next
                if not current.next:
                    self.tail = current
                return deleted_data
            current = current.next
        return None
    
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def get_linked_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

print('🌿 Innisfree Green Tea "Go Plump Challenge" 🌿')
go_plump = LinkedLists()

go_plump.insert_at_end("plump🫧")
go_plump.insert_at_end("glowing✨")
go_plump.insert_at_beginning("cleanse🫧")
go_plump.insert_at_beginning("tone🍃")
go_plump.insert_at_end("hydration🌊")
go_plump.insert_at_end("boost!☀️")
go_plump.insert_at_end("selfie📸")

print(go_plump.remove_beginning())
print(go_plump.remove_at_end())
print(go_plump.remove_at("cleanse🫧"))
print(go_plump.remove_at("mist ☁️"))
print(go_plump.search("tone🍃"))
print(go_plump.search("hydration🌊"))

print(go_plump.get_linked_list())
