"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

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

# helper for testing: pass in the first node (head) and all the elements should be printed
def print_list(head: LinkedListNode):
    current_node = head
    while current_node:
        print(current_node.value)
        current_node = current_node.next #traverse to the next node until current_node.next = None
    print("End of List")

# Plan:
# can only look forward for a given node
# change the previous node's next pointer to "skip over" the given node as a way of deleting it
# with we can't look back, can't access previous node in without traversing n times
# Can achieve the same effect by assigning the given node the value of the next node and also its pointer(next property)
# this will skip turn the given node into given_node.next and skip over the next node

def delete_node(node):
    # edge case: check if next is undefined before proceeding, can't access None.next
    next = node.next
    if next:
        node.value = next.value
        node.next = next.next
    else:
        print("Error: node argument is the last element of list")
        node = None
    


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z
# list created X -> Y -> Z

print_list(x)

delete_node(y) # X -> Z

print_list(x)

# edge case: delete from end of the list
delete_node(z)
print_list(x)
