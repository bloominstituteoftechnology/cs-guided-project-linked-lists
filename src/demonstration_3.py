"""
Given a non-empty, singly linked list with a reference to the head node, return a middle node of linked list. If there are two middle nodes, return the second middle node.

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list
The returned node has value 3.
Note that we returned a `ListNode` object `ans`, such that:
`ans.val` = 3, `ans.next.val` = 4, `ans.next.next.val` = 5, and `ans.next.next.next` = NULL.

Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list
Since the list has two middle nodes with values 3 and 4, we return the second one.

*Note: The number of nodes in the given list will be between 1 and 100.*
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(self, head):
    # Your code here

