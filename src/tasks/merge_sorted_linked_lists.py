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

# given two SLL l1 and l2, both contain integers sorted in ascending order:
# merge the two lists into one list also sorted in ascending order that contains all nodes from both original lists
# solution must be O(l1 + l2) time complexity
# return new SLL

def sll_merge(l1, l2):
    # create pointers for current l1, l2 initialized at respective heads
    current_l1 = l1
    current_l2 = l2
    # pointer for new list node head and current new list node
    new_list_head = None
    current_new_node = None
    # while loop through, condition: if current_l1 and current_l2
    while current_l1 and current_l2:
        if current_l1.value <= current_l2.value:
            # create new_node using current_l1.value
            new_node = ListNode(current_l1.value)
            if new_list_head is None:
                # set new_list_head to new_node
                new_list_head = new_node
                # set current_new_node to new_node
                current_new_node = new_node
                # set current_l1 to current_l1.next
                current_l1 = current_l1.next

            else:
                # link new_node to new linked list
                current_new_node.next = new_node
                # set current_new_node to new_node
                current_new_node = new_node
                # set current_l1 to current_l1.next
                current_l1 = current_l1.next

        # else current l1 is greater than current_l2
        else:
            # create new_node using current_l2.value
            new_node = ListNode(current_l2.value)
            if new_list_head is None:
                # set new_list_head to new_node
                new_list_head = new_node
                # set current_new_node to new_node
                current_new_node = new_node
                # set current_l2 to current_l2.next
                current_l2 = current_l2.next
            else:
                # current_new_node.next = new_node
                current_new_node.next = new_node
                # current_new_node = new_node
                current_new_node = new_node
                # current_l2 = current_l2.next
                current_l2 = current_l2.next
    # loop has broken because current_l1 or current_l2 is None

    if current_l1 is None:
        # while loop through starting at current_l2
        while current_l2:
            # create new_node for current_l2
            new_node = ListNode(current_l2.value)
            if new_list_head is None:
                new_list_head = new_node
                current_new_node = new_node
                current_l2 = current_l2.next
            else:
                # link new_node to the new list
                current_new_node.next = new_node
                # move the current_new_node pointer
                current_new_node = new_node
                # move the current_l2 pointer
                current_l2 = current_l2.next
    # else current_l2 is None, we need to start loop at current_l1 and add, change to if????
    else:
        # while loop through starting at current_l1
        while current_l1:
            # create new_node for current_l1
            new_node = ListNode(current_l1.value)
            if new_list_head is None:
                new_list_head = new_node
                current_new_node = new_node
                current_l1 = current_l1.next
            else:
                # link new_node to the new list
                current_new_node.next = new_node
                # move the current_new_node pointer
                current_new_node = new_node
                # move the current_l1 pointer
                current_l1 = current_l1.next

    # return the new list    
    return new_list_head


# test case
l1_head = ListNode(1)
l1_node_2 = ListNode(1)
l1_head.next = l1_node_2
l1_node_3 = ListNode(2)
l1_node_2.next = l1_node_3
l1_node_4 = ListNode(4)
l1_node_3.next = l1_node_4
print('-------l1-------')
print_list(l1_head)
print('-------l2-------')
l2_head = ListNode(0)
l2_node_2 = ListNode(3)
l2_head.next = l2_node_2
l2_node_3 = ListNode(5)
l2_node_2.next = l2_node_3
print_list(l2_head)

print('-------merged list-------')
print_list(sll_merge(l1_head, l2_head))

