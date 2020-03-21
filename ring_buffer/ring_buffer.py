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
        if self.storage.length < 3:
            self.storage.add_to_tail((item, 0))

        print(self.storage)
        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

myRing = RingBuffer(3)
myRing.append("a")
myRing.append("b")
myRing.append("c")
myRing.append("d")






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
# sort the array by age count. Return the array

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
