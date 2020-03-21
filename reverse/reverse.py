class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def __str__(self):
    if self.head is None:
        return "empty"
    curr_node = self.head
    # "(3) <-> (5) <-> ..."
    output = ""
    output += f'({curr_node.value})'
    while curr_node.next_node is not None:
        curr_node = curr_node.next_node
        output += f' <-> ({curr_node.value})'
    return output

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    curr_node = self.head
    if curr_node is not None:
      hold_next = self.head.next_node
    while curr_node is not None:
      curr_node.next_node = None
      curr_node = hold_next
      if curr_node is not None:
        hold_next = hold_next.next_node
        self.add_to_head(curr_node.value)
    pass

# myList = LinkedList()
# myList.add_to_head(1)
# myList.add_to_head(2)
# myList.add_to_head(3)
# myList.add_to_head(4)
# myList.add_to_head(5)
# print(myList)

# myList.reverse_list()

# print(myList)

# Understand:
# Get a single linked list and reverse it
# (1)->(2)->(3)->None would then become (3)->(2)->(1)->None

# Plan:
# delete and move to head each item going next untill you reach none.