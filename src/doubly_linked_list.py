class ListNode:
    """
    Each ListNode holds a reference to its previous node
    as well as its next node in the List. That two-directional
    reference is what allows for our DoublyLinkedList to be
    doubly-linked
    """
​
    def __init__(self, value, prev=None, next=None):
        """Construct a node that stores the specified value.
​
        prev and next references are optional on construction and default
        to None if nothing else is specified
        """
​
        self.prev = prev  # the node before this one — defaults to None
        self.value = value  # the value to store
        self.next = next  # the node after this one — defaults to None
​
    def __repr__(self):
        return f"ListNode({self.value})"
​
​
class DoublyLinkedList:
    """
    Our doubly-linked list class. It holds references to
    the list's head and tail nodes as well as the list's size
    """
​
    def __init__(self, node=None):
        self.head = node  # the first item in list
        self.tail = node  # the last item in list
        self.size = 1 if node is not None else 0  # number of items stored in DLL
​
    def __len__(self):
        return self.size
​
    def __repr__(self):
        """Returns a string representation of this DoublyLinkedList"""
        if self.size == 0:
            return "DLL=[]"
​
        str_repr = "DLL=["
        current_node = self.head
​
        while current_node is not None:
            str_repr += f"{current_node} -> "
            current_node = current_node.next
​
        str_repr = f"{str_repr[:-4]}]"
        return str_repr
​
    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly.
        """
​
        new_node = ListNode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
​
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
​
        # increments the size attribute after adding node to list
        self.size += 1
​
    def remove_from_head(self):
        """
        Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        """
​
        if self.size == 0:  # no elements in list
            return None  # nothing to return
​
        removed_value = self.head.value  # make a copy of the node to be deleted
​
        if self.size == 1:  # if only one element in list (node is head and tail)
            self.head = self.tail = None  # list will be empty
​
        else:  # more than one element in list
            self.head = self.head.next  # shift head right (reassign head to head.next)
            self.head.prev = None  # reassign head.prev to point at None (it used to point at old_head)
​
        self.size -= 1
        return removed_value
​
    def add_to_tail(self, value):
        """
        Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly.
        """
​
        new_node = ListNode(value)
​
        if self.size == 0:  # if list is empty
            self.head = self.tail = new_node  # make new_node both head and tail
​
        else:
            self.tail.next = new_node  # place new_node after tail
            new_node.prev = self.tail  # place current tail before new_node
            self.tail = new_node  # replace self.tail
​
        self.size += 1  # increase size of list
​
    def remove_from_tail(self):
        """
        Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
​
        if self.size == 0:  # if list is empty
            return None  # nothing to remove; return out
​
        tail_to_remove = self.tail  # copy value of current tail before deletion (for return)
        tail_to_remove.prev = tail_to_remove.next = None  # remove any ties to list
​
        if self.size == 1:  # if only one item in list
            self.head = self.tail = None  # list will now be empty
​
        else:
            self.tail.prev.next = None  # reassign new tail's prev to None (last item)
            self.tail = self.tail.prev  # shift tail left
​
        self.size -= 1  # decrease size (deleting el)
        return tail_to_remove.value  # return value of removed tail
​
    def move_to_front(self, node):
        """
        Removes the input node from its current spot in the
        List and inserts it as the new head node of the List.
        """
​
        if self.size == 0:  # no items in list
            return  # nothing to move; return out
​
        if self.head is node:  # if node is head already
            return  # nothing to move, node is at beginning; return out
​
        if self.tail is node:  # if node is tail
            self.tail = node.prev  # shift tail left
​
        else:  # else node must not be tail
            # if node is not tail, then node.next is not None
            node.next.prev = node.prev  # sew node.next to node.prev
​
        node.prev.next = node.next  # if node=tail next is None; else, next is a node. Works either way!
        self.head.prev = node  # assign current head's prev to point at node instead of None
        node.next = self.head  # place node before head
        self.head = node  # reassign head (shifting left) head is now node
        self.head.prev = None  # reassign head.prev to point at None (no nodes before head)
​
    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List.
        """
​
        if self.size == 0:  # no items in list
            return  # there is no such node
​
        if node is self.tail:  # node is already at end as it is the tail
            return  # node does not need to be moved
​
        if node is not self.head:
            # node must be in the middle of list (node is neither head nor tail, list is not empty)
            node.prev.next = node.next  # since node is not head, deal with node.prev
​
        else:  # if node is at the beginning of the list
            self.head = node.next
​
        node.next.prev = node.prev  # assign the next_node's prev pointer to point at prev_node
        self.tail.next = node  # point current_tail.next at node
        node.prev = self.tail  # point node.prev at current_tail
        node.next = None  # assign node.next none as it will be tail (and thus at end of list)
        self.tail = node  # assign node as tail
​
    def delete(self, node):
        """
        Deletes the input node from the List, preserving the
        order of the other elements of the List.
        """
​
        if self.size == 0:  # if list is empty
            return None  # nothing to delete
​
        removed_value = node.value  # copy deleted node's value
​
        if self.size == 1:  # if only one item in list
            self.head = self.tail = None
            self.size -= 1
​
        else:  # more than one element in list
            if self.head is node:  # node to delete is head
                self.head = node.next  # reassign head to be element after head
​
            elif self.tail is node:  # node to delete is tail
                self.tail = node.prev  # reassign tail to be element before tail
​
            else:  # node is neither head nor tail, putting it somewhere in the middle
                node.prev.next = node.next
                node.next.prev = node.prev
​
            node.next = node.prev = None
            self.size -= 1
​
        return removed_value
​
    def get_max(self):
        """Finds and returns the maximum value of all the nodes
        in the List."""
​
        max_value = self.head.value
        current_node = self.head
        # while current_node.next is not None: # when current_node = current.tail, this will not iterate
        while current_node.next is not None:  # when current_node = current.tail, this will not iterate
            current_node = current_node.next
            # checks if the value is larger than our max value so far
            if max_value < current_node.value:
                max_value = current_node.value
        return max_value
