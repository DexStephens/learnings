class LinkedList:
    def __init__(self, node) -> None:
        self.head = node
    
    def append(self, node):
        current = self.head
        while (current.next is not None):
            current = current.next
        
        current.next = node
    
    def get(self, value):
        current = self.head
        while (current.next is not None):
            if current.value == value:
                return current
            current = current.next
        return None


class LinkedListNode:
    def __init__(self, value):
        self.next = None
        self.value = value