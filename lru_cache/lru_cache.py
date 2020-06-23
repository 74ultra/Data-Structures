from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList()
        self.lookup = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if the key is not in the lookup, return none
        node = self.lookup.get(key)
        if node == None:
            return None
        else:
            self.storage.move_to_end(node)
            return node.value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # check lookup to see if value already exists
        if not self.lookup.get(key):
            # check limit to see if a value needs to be discarded
            if self.size == self.limit:
                # remove the head and remove from lookup
                removed = self.storage.remove_from_head()
                self.lookup.pop(removed[0])
                self.size -= 1
            self.storage.add_to_tail(key, value)
            self.lookup[key] = self.storage.tail
            self.size += 1
        # if value already exists, it is overwritten by new node
        else:
            node_new_value = self.lookup[key]
            node_new_value.value = value
            self.storage.move_to_end(node_new_value)


# xer = LRUCache()
# xer.set('key', 1)
# xer.set('keys', 2)
# xer.set('more', 3)
# xer.set('mores keys', 4)
# xer.set('smore keys', 5)
# xer.set('lmore keys', 6)
# xer.set('xmore keys', 7)
# xer.set('amore keys', 8)
# xer.set('bmore keys', 9)
# xer.set('cmore keys', 10)
# print('head', xer.storage.head.value)
# print('tail', xer.storage.tail.value)
# print('get value:', xer.get('key'))
# print('head', xer.storage.head.value)
# print('tail', xer.storage.tail.value)

# xer.set('keys', 222)

# print('head', xer.storage.head.value)
# print('tail', xer.storage.tail.value)
