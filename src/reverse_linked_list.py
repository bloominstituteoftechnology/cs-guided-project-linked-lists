"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
#test commit
# example list 1->2->3->4->5 turns into 5->4->3->2->1
# input is the head node, in example that would be 1
# O(1) space, can't make new list
# O(1) time, traverse the list only once

# description of what nodes look like
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

# import some functions from our example linked list file
from review_lecture_notes import add_node_to_next, print_list_iteratively

def reverse(head_of_list):
    # if list is empty or contains only one node, return it
    if not head_of_list or not head_of_list.next:
        return head_of_list
    
    # pointers to keep track of
    # where we are
    current_node = head_of_list
    # where we came from
    previous_node = None
    # because of the overwriting, we need to store this to keep the while loop going
    next_node = None

    # all three pointers need to by shifted over one at a time in order to change the whole list
    # move previous_node first, current_node second, and next_node last to keep the links we need to traverse the whole list
    while current_node: # run the loop as long as we haven't gotten to the end of the list
        # cache the next node before resetting the next property on current node to point backwards
        next_node = current_node.next
        # point our current_node to the previous_node (backwards), "flip the arrow"
        current_node.next = previous_node
        # shuffle previous_node to current_node for the next round
        previous_node = current_node
        # move to the next_node
        current_node = next_node
    # when loop finishes, return the head
    return previous_node

# create an example list to work with
head = LinkedListNode(1)
tail = head

tail = add_node_to_next(tail, 2)
tail = add_node_to_next(tail, 3)
tail = add_node_to_next(tail, 4)
tail = add_node_to_next(tail, 5)

print_list_iteratively(head)
print('-------------------')
reversed_list_head = reverse(head)
print_list_iteratively(reversed_list_head)
