"""
Linked List
    - get/access
    - insert
    - delete
    - search (traversal)

    * space complexity = O(n)

Linear data structure
    - items are ordered

The beginning of the linked list is called the head and the end is called the tail. Appending a node would be adding to the head.
"""

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None # Another node

def add_to_head(head, value):
    # create the new node
    new_node = LinkedListNode(value)
    # Link the new node, to the head
    new_node.next = head
    return new_node # the start of the linked list

def add_to_tail(tail, value):
    # create the new node
    new_node = LinkedListNode(value)
    # Link the new node, to the tail
    tail.next = new_node
    return new_node # the end of the linked list

def add_to_next(current_node, value):
    # create the new node
    new_node = LinkedListNode(value)
    next_node = current_node.next
    # current node points to new node
    current_node.next = new_node
    new_node.next = next_node

# def print_list(start_node):
#     if start_node is None:
#         return

#     print(start_node.value)
#     print_list(start_node.next)

def print_list(start_node):
    curr_node = start_node

    while curr_node is not None:
        print(curr_node.value)
        # update current node to next
        curr_node = curr_node.next

# linked_list = LinkedListNode(3)
# tail = linked_list

# linked_list = add_to_head(linked_list, 2)
# linked_list = add_to_head(linked_list, 5)
# middle = linked_list
# linked_list = add_to_head(linked_list, 6)
# linked_list = add_to_head(linked_list, 0)

# tail = add_to_tail(tail, 12)
# add_to_next(middle, 7)

# # print_list(linked_list)

# print_list(middle)

# linked_list.next = LinkedListNode(2)
# linked_list.next.next = LinkedListNode(6)
# linked_list.next.next.next = LinkedListNode(5)