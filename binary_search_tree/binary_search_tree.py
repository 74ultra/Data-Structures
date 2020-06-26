from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if there is a root
        # if self is None:
        #     self = BSTNode(value)
        # compare the value to root's value to determine search direction
        if value < self.value:
            # go left
            if self.left:
                # self.left exists
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            # go right
            if self.right:
                # self.right exists
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                # --> returning the function is necessary to have its result returned
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    def contains_lecture(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self.value
        if self.right:
            return self.right.get_max()
        else:
            return max_val

    def get_max_lecture(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # depth-first follows LIFO ordering of its nodes
    def iter_depth_first_for_each(self, fn):
        # init stack to keep track of order of nodes visited
        stack = []
        # add first node to stack
        stack.append(self)
        # continue traversing until the stack is empty
        while len(stack) > 0:
            # pop off the stack
            current_node = stack.pop()
            # add its children to the stack (right then left to ensure proper order)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            # call the fn function on self.value
            fn(self.value)

    # breadth-first traversal follows FIFO ordering
    def iter_breadth_first_for_each(self, fn):
        q = deque()
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     if node == None:
    #         return
    #     self.in_order_print(node.left)
    #     print(node.value)
    #     self.in_order_print(node.right)

    def in_order_print(self, node):
        if node == None:
            return
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque()
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node == None:
            return
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)


xer = BSTNode(51)
for i in range(1, 104):
    if i % 2 == 0:
        xer.insert(i)

for i in range(1, 104):
    if i % 2 != 0:
        xer.insert(i)

# # def temp_cb(val):
# #     print(2 * val)

xer.in_order_print(xer)
# print(xer.contains(126))
