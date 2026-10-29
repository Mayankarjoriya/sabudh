
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUcache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node:None):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node:Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self,key:int):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key:int, value:int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self._add(new_node)

            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]


lruCache = LRUcache(2)
lruCache.put(1,1)
lruCache.put(2,2)
print(lruCache.get(1))
lruCache.put(3,3)
print(lruCache.get(2))
lruCache.put(4,4)

print(lruCache.get(1))
print(lruCache.get(3))
print(lruCache.get(4))