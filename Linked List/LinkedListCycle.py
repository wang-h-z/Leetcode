# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Using Hash Table
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map = dict()
        while head: 
            if head in map: 
                return True
            else: 
                map[head] = 0
            head = head.next
        return False

# Using Floyd's Cycle Finding Algorithm / Tortoise and Hare algorithm
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True