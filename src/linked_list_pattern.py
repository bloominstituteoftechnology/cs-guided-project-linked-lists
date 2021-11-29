# lets represent a Node 
class LinkedListNode:
    # constructor
    def __init__(self, value):
        self.value = value
        # the "arrow"
        self.next = None
# initialized a few LinkedListNodes
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
# connect the LinkedListNodes together
x.next = y
y.next = z
# define a function that prints every node in the linked list starting with the input node
def print_ll(node):
    #init a new ref that will keep track of where we are in the traversal 
    current = node
    # traverse the linked list until we get to the end 
    # print the value of each node along the way
    while current is not None:
        print(current.value)
        # update current to refer to the next node in the Linked List
        current = current.next
print_ll(x)