"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
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

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            removed_head = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_head
        else:
            removed_head = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return removed_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
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

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            removed_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return removed_tail.value
        else:
            removed_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return removed_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

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

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

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
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

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

    """Returns the highest value currently in the list"""

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


# xer.add_to_tail(1)
# # xer.add_to_tail(2)
# # xer.add_to_tail(3)
# # xer.add_to_tail(4)
# print(xer.remove_from_tail())
# print(xer.head, xer.tail)
# print(xer.head.value, xer.head.next.value, xer.tail.prev.value, xer.tail.value)

# xer.move_to_end(xer.head.next.next)

# print(xer.head.value, xer.head.next.value, xer.tail.prev.value, xer.tail.value)

# print(xer.head.prev, xer.head.next)
