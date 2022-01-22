
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# helper to print:
def print_list(start_node):
    current_node = start_node
    while current_node:
        print(current_node.value)
        current_node = current_node.next

# given a singly linked list, of which l is the head, which is already sorted in ascending order and an integer called value
# add value to the linked list in the correct spot to preserve the ascending sort order
# all integer values in the list are unique
# guaranteed the value passed in is not already in the linked list
# return l after inserting the value into the list
# solution must be O(n) time where n is the number of nodes in l

def insert_into_sorted_list(l, value):
    # init pointers
    current_node = l
    # create new node with value
    new_node = ListNode(value)
    # while loop through the list
    while current_node:
        # if current_node.value is greater than value
        if current_node.value > value:
            # point new_node to current node
            new_node.next = current_node
            # set start_node to new_node
            return new_node
        # current_node.next.value is None
        elif current_node.next is None:
            # point current_node.next to new_node
            current_node.next = new_node
            # return out
            return l
        # if current_node.next.value is greater than value
        elif current_node.next.value > value:
            # save current_node.next
            node_after_insert = current_node.next
            # link current_node to new_node with value arg
            current_node.next = new_node
            # link new_node to saved node
            new_node.next = node_after_insert
            # return out
            return l
        # current_node.naxt.value is less than value
        # set current_node to current_node.next to continue loop
        current_node = current_node.next
    # loop has broken, l isn't a node, return new_node
    return new_node


# test cases
# For l = [1, 3, 4, 6] and value = 5, the output should be
# solution(l, value) = [1, 3, 4, 5, 6]
test_case_head = ListNode(1)
tc_node_2 = ListNode(3)
test_case_head.next = tc_node_2
tc_node_3 = ListNode(4)
tc_node_2.next = tc_node_3
tc_node_4 = ListNode(6)
tc_node_3.next = tc_node_4
print_list(test_case_head)
print('-----after running insert 5-----')
print_list(insert_into_sorted_list(test_case_head, 5))
print('-----after running insert 0-----')
print_list(insert_into_sorted_list(test_case_head, 0))
print('-----after running insert 999-----')
print_list(insert_into_sorted_list(test_case_head, 999))
