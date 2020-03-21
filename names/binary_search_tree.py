import sys

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return

        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)
        # compare value to the current node
        # if smaller, go left
        # if bigger, go right

        # if no node to go to, (either left or right)
            # make the new node at that spot

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
       
        # --- recurse ---
        # compare value to the current node value
        # if smaller, go left
        # if bigger, go right
        # if equal, return True!
        # --- recurse ---
        
        # if smaller, but can't go left, return false
        # if larger, but can't go right, return false

    # Return the maximum value found in the tree
    def get_max(self):
        # get the value to the most right
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # left first
        if node.left is not None:
            node.left.in_order_print(node.left)

        print(node.value)

        # print right second
        if node.right is not None:
            node.right.in_order_print(node.right)
        pass
