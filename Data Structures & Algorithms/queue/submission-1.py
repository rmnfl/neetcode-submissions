class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = ListNode(value)

        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        value = self.tail.prev.val

        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        
        return value
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
            
        value = self.head.next.val

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

        return value
