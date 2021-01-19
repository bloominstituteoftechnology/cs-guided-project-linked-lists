class Node:
    def __init__(self, val, nxt=None):  # Constructor
        self.value = val
        self.next = nxt
​
    def __repr__(self):
        return f'Node({repr(self.value)})'
​
​
head = None
​
def insert_at_front(val):
    global head
​
    # Make a new node
    new_node = Node(val)
​
    # Point new node next at head
    new_node.next = head
​
    # Point head to new node
    head = new_node
​
def print_list():
    global head
​
    # Set cur to head
    cur = head
​
    # Loop while cur.next is not None
    while cur is not None:
        # Print value at cur
        print(cur.value, end=" ")
​
        # Set cur to cur.next
        cur = cur.next
​
    print()
​
def delete_head():
    global head
​
    old_next = head.next
    head.next = None
​
    head = old_next
​
def delete_node(value):
    global head
​
    # Special case: empty list
    if head is None:
        return
​
    # Special case: delete the head
    if head.value == value:
        delete_head()
        return
​
    # General case of deleting something in the middle
    prev = head
    cur = head.next
​
    while cur is not None:
        if cur.value == value:
            #print(f"Found it! {prev.value}, {cur.value}")
            prev.next = cur.next
            cur.next = None
            return
​
        cur = cur.next
        prev = prev.next
​
    print("Didn't find it")
​
​
insert_at_front(45)
insert_at_front(88)
insert_at_front(24)
insert_at_front(12)
​
print_list()
​
#delete_node(88)
delete_node(12)
​
print_list()
​
#delete_head()
​
#print_list()
