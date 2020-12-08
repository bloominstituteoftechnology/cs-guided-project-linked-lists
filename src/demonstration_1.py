"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.
Example:
The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked
list by calling the function `delete_node`. It is your job to write the `delete_node` function.
```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
x.next = y
y.next = z
delete_node(y)
```
*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None
def delete_node(node_to_delete):
    """
    Input: a reference to a node in a linked list that we want
    to delete from the linked list
    Output: this function will mutate the linked list but it
    won't return anything
    One way we can delete a node from a linked list is to change
    the node that refers to the node we want to delete so that it
    points to the node we want to delete next node
    We need access to the node that refers to the node we want to
    delete
    So we're replacing the 'node_to_delete', and then deleting the 
    next node
    1. Changed the 'node_to_delete' value to its next node's value
    2. Remove the 'node_to_delete' next node by having 'node_to_delete'
       next refer to the next node's next
    """
    next_node = node_to_delete.next
    # set the 'node_to_delete' value to its next node's value
    node_to_delete.value = next_node.value
    # set 'node_to_delete' next to the next node's next
    node_to_delete.next = next_node.next
# define a function that prints every node
# in the linked list starting with the node
def print_ll(node):
    # init a new reference that will keep track
    # of where we are in the traversal
    current = node
    # traverse the linked list until
    # we get to the end
    while current is not None:
        # print the value of each node along the way
        print(current.value)
        # update current to refer to the next node
        # in the linked list
        current = current.next
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
x.next = y
y.next = z
print_ll(x)
delete_node(y)
print_ll(x)