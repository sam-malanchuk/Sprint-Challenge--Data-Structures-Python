from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length > 0:
            curr_node = self.storage.head
            while curr_node is not None:
                curr_item = curr_node.value[0]
                curr_count = curr_node.value[1] + 1
                curr_node.value = (curr_item, curr_count)
                curr_node = curr_node.next
        if self.storage.length < self.capacity:
            self.storage.add_to_tail((item, 0))
        if self.storage.length == self.capacity:
            curr_node = self.storage.head
            while curr_node is not None:
                if curr_node.value[1] == self.capacity:
                    curr_node.value = (item, 0)
                curr_node = curr_node.next
        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr_node = self.storage.head
        while curr_node is not None:
            list_buffer_contents.append(curr_node.value[0])
            curr_node = curr_node.next

        return list_buffer_contents

# Understand
# Create a class that will accept a capacity parameter, then accept the append of
# additional values, each value fills up a slot to the max capacity.
# When max capacity is reached, then start replacing the oldest value
# get() method, for any value that is not None, put it in an array and return in
# the correct order, oldest to newest

# Plan
# append(): if self.storage.length < 3 then add the value with a old variable counter of 0
# if self.storage.length == 3 then check each node in storage to find oldest,
# then replace it with the new value and a fresh count of 0
# in both cases up everyone elses count +1
# get(): run through the storage from head getting each node and putting into the array,
# Return the array

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
