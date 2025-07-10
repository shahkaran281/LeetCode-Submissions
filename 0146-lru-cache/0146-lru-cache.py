class DLL:

    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.first = DLL()
        self.last = DLL()
        self.first.next = self.last  # Most recent
        self.last.prev = self.first  # Least recent
        self.keyToNode = dict()

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            node = self.keyToNode[key]

            # Remove node from current position
            node.prev.next = node.next
            node.next.prev = node.prev

            # Insert node right after head (most recent)
            node.next = self.first.next
            node.prev = self.first
            self.first.next.prev = node
            self.first.next = node

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value

            # Move node to front
            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.first.next
            node.prev = self.first
            self.first.next.prev = node
            self.first.next = node

        else:
            if len(self.keyToNode) == self.cap:
                # Evict least recently used node
                lastNode = self.last.prev
                lastNode.prev.next = self.last
                self.last.prev = lastNode.prev
                del self.keyToNode[lastNode.key]

            # Add new node to front
            node = DLL(key=key, val=value)
            node.prev = self.first
            node.next = self.first.next
            self.first.next.prev = node
            self.first.next = node
            self.keyToNode[key] = node
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)