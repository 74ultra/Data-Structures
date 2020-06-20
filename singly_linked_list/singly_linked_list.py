

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
            current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None
        current_node = self.head
        max_value = self.head.value
        while current_node.next_node is not None:
            if current_node.value < current_node.next_node.value and current_node.next_node.value > max_value:
                max_value = current_node.next_node.value
                current_node = current_node.next_node
            else:
                current_node = current_node.next_node

        return max_value


# xer = LinkedList()
# xer.add_to_head(34)
# xer.add_to_head(24)
# xer.add_to_head(2224)
# xer.add_to_head(123434)
# xer.add_to_head(56724)
# xer.add_to_head(23834)
# xer.add_to_head(24)
# xer.add_to_head(134)
# xer.add_to_head(222224)
# xer.add_to_head(34)
# xer.add_to_head(2467)


# print(xer.get_max())
