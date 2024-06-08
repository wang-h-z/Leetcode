class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases smoothly
        dummy = ListNode(0, head)
        pointer = head
        counter = 0
        
        # Count the total number of nodes in the list
        while pointer:
            pointer = pointer.next
            counter += 1
        
        steps = counter - n
        current = dummy  # Start from the dummy node
        
        # Move to the node right before the one we want to remove
        for _ in range(steps):
            current = current.next
        
        # Remove the nth node from the end
        current.next = current.next.next
        
        # Return the head of the modified list
        return dummy.next


