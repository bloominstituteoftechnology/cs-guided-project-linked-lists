# Create a linked list node class

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None # other LinkedListNode address

# head and tail are two variables that give us access to the rest of the list
# linked list is only as good as the first (and last) nodes you have access to

# start the new node list at head
head = LinkedListNode('A')

# end node list at tail (since we only have the head item, it serves as both the beginning and end of the list)
tail = head

# take in node and a value and attach a new node to the end of it
def add_node_to_next(current_node, value):
    # make the new node
    new_node = LinkedListNode(value)

    # before breaking the link to the old version of next, save it as a variable in case we need it
    old_next = current_node.next

    # attach the new_node to the current_node
    current_node.next = new_node

    # new_node should link to whatever current_node was liked to before
    new_node.next = old_next

    # return new_node so it can be used to set the tail
    return new_node

print('stock tail.next-->', tail.next)
# invoke add_node_to_next to link a new node to tail.next
tail = add_node_to_next(tail, 'B')

tail = add_node_to_next(tail, 'C')

# add node after head but before tail
add_node_to_next(head, 'E')

# create a functionto add a new node at begininng of linked list
# move what head points to
def add_node_to_head(current_head, value):
    # unlinked new_node created, links to nothing at this point
    new_head = LinkedListNode(value)
    # assign its next property to point to the existing head
    new_head.next = current_head
    # return the new head node so it can be reassigned
    return new_head

# function to print the list recursively
def print_list_recursively(start_node):
    # if start_node is None, return out
    if not start_node:
        return
    # start_node is not None, print it
    print(start_node.value)
    # recursively call our print function on the current argument's next property
    # if it is None it will be returned out in this call before it hits the print statement
    print_list_recursively(start_node.next)

# function to print the list iteratively
def print_list_iteratively(start_node):
    # create pointer for the current_node
    current_node = start_node
    while current_node:
        print(current_node.value)
        current_node = current_node.next

# function to get a specific node index
def get_nth_node(start_node, n):
    current_node = start_node
    current_node_idx = 0
    while current_node:
        if current_node_idx == n:
            return current_node
        current_node = current_node.next
        current_node_idx += 1

# reassign head variable new_head and it will now point to the old head and thus the rest of the linked list chain
head = add_node_to_head(head, 'D')
print("new head-->", head.value)
print("old head-->", head.next.value)

# print our list recursively
print_list_recursively(head)

# print our list iteratively
print_list_iteratively(head)

# get 4th node
fourth = get_nth_node(head, 3)
print('fourth node', fourth.value)