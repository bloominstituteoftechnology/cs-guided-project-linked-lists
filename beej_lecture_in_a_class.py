class Node:
    def __init__(self, val, nxt=None):  # Constructor
        self.value = val
        self.next = nxt
​
    def __repr__(self):
        return f'Node({repr(self.value)})'
​
class LinkedList:
    def __init__(self):
        self.head = None
​
    def __str__(self):
        # Pretty print
        s = ""
        cur = self.head
​
        while cur is not None:
            s += str(cur.value)
            if cur.next is not None:
                s += " -> "
            cur = cur.next
​
        return s
​
    def insert_at_front(self, val):
        # Make a new node
        new_node = Node(val)
​
        # Point new node next at head
        new_node.next = self.head
​
        # Point head to new node
        self.head = new_node
​
    def print_list(self):
        # Set cur to head
        cur = self.head
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
    def delete_head(self):
        old_next = self.head.next
        self.head.next = None
​
        self.head = old_next
​
    def delete_node(self, value):
        # Special case: empty list
        if self.head is None:
            return
​
        # Special case: delete the head
        if self.head.value == value:
            self.delete_head()
            return
​
        # General case of deleting something in the middle
        prev = self.head
        cur = self.head.next
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
ll = LinkedList()
​
ll.insert_at_front(45)
ll.insert_at_front(88)
ll.insert_at_front(24)
ll.insert_at_front(12)
​
print(ll)
​
ll.delete_node(12)
​
print(ll)
