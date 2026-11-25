class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    
    def __init__(self, capacity: int):
        self.table = [None] * capacity
        self.capacity = capacity
        self.size = 0


    def insert(self, key: int, value: int) -> None:
        index = self._hash(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            prev, curr = None, node
            while curr:
                if node.key == key:
                    node.value = value
                    return
                prev, curr = curr, curr.next
            
            prev.next = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        index = self._hash(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return -1


    def remove(self, key: int) -> bool:
        index = self._hash(key)

        prev, curr = None, self.table[index]
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[index] = None
                self.size -= 1
                return True
            prev, curr = curr, curr.next

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next

        self.capacity = new_capacity
        self.table = new_table


    def _hash(self, key):
        return key % self.capacity

