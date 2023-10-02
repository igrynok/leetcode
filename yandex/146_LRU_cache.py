class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.volume = 0
        self.map = {}
        self.head = None
        self.tail = None

    def move_to_head(self, node: Node) -> None:
        # remove
        if node == self.tail:
            self.tail = self.tail.prev
        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        # move to head
        node.next = self.head
        self.head.prev = node
        self.head = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            if node is not self.head:
                self.move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:

        if self.volume == self.capacity and key not in self.map:
            del self.map[self.tail.key]
            if self.tail is not self.head:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                self.head = self.tail = None
            self.volume -= 1

        if key in self.map:
            node = self.map[key]
            node.val = value
            if node is not self.head:
                self.move_to_head(node)
        else:
            n = Node(value, key)
            if self.head is not None:
                self.head.prev = n
                n.next = self.head
            else:
                self.tail = n
            self.head = n
            self.map[key] = n

            self.volume += 1

        # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)