

class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, key, value):
        current_next = self.next
        self.next = ListNode(key, value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, key, value):
        current_prev = self.prev
        self.prev = ListNode(key, value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, key, value):
        new_node = ListNode(key, value, None, None)
        if self.head is None and self.tail is None:  # possibly - if not self.head and not self.tail
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # # the NEXT property of the new node is set to the current head node
            # new_node.next = self.head
            # # the PREV property of the current head is set to the new node
            # self.head.prev = new_node
            # # the new node is set to be the head
            # self.head = new_node
            # self.length += 1

            current_head = self.head
            self.head = new_node
            self.head.next = current_head
            self.head.next.prev = self.head
            self.length += 1

    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            removed_head = [self.head.key, self.head.value]
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_head
        else:
            removed_head = [self.head.key, self.head.value]
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return removed_head

    def add_to_tail(self, key, value):
        new_node = ListNode(key, value, None, None)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            prev_tail = self.tail
            self.tail = new_node
            self.tail.prev = prev_tail
            prev_tail.next = self.tail
            self.length += 1

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            removed_tail = [self.tail.key, self.tail.value]
            self.tail = None
            self.head = None
            self.length -= 1
            return removed_tail
        else:
            removed_tail = [self.tail.key, self.tail.value]
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return removed_tail

    def move_to_front(self, node):
        if self.head == node:
            return None
        if self.tail == node:
            # current_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            current_head = self.head
            self.head = node
            self.head.next = current_head
        else:
            # NEXT pointer from previous node pointed at new Next
            node.prev.next = node.next
            # PREV pointer from next node pointed at new prev
            node.next.prev = node.prev
            current_head = self.head
            self.head = node
            self.head.next = current_head
            self.head.prev = None
            current_head.prev = self.head

    def move_to_end(self, node):
        if self.tail == node:
            return None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
            current_tail = self.tail
            self.tail = node
            self.tail.prev = current_tail
            current_tail.next = self.tail
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            current_tail = self.tail
            self.tail = node
            self.tail.next = None
            self.tail.prev = current_tail
            current_tail.next = self.tail

    def delete(self, node):
        if self.head == self.tail and self.head == node:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def get_max(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            return self.head.value
        current_node = self.head
        max_value = self.head.value
        while current_node.next is not None:
            if current_node.value < current_node.next.value and current_node.next.value > max_value:
                max_value = current_node.next.value
                current_node = current_node.next
            else:
                current_node = current_node.next

        return max_value


# xer = DoublyLinkedList()
# xer.add_to_head('cars', 3)
# xer.add_to_head('kids', 2)
# print(xer.head.key, xer.head.value)
