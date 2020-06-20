class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node.value
        return False

    def remove_tail(self):
        # check for an empty list
        if not self.head:
            return None
        # check if list only contains one item
        if self.head is self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            return value
        # prepare to loop through nodes
        current = self.head
        # checks each node to see if the next node is the tail
        while current.next_node is not self.tail:
            current = current.next_node

        value = self.tail.value
        # the next to last node is set as the tail
        self.tail = current
        # the new tail's next_node is set to be None
        self.tail.next_node = None
        return value
