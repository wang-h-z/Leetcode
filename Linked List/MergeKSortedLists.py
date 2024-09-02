import heapq
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(None)
        current = dummy
        
        for pos, node in enumerate(lists):
                if node: 
                    heapq.heappush(heap, (node.val,pos,node))
        
        while heap: 
            val, pos, node = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next 
            node = node.next
            if node: 
                heapq.heappush(heap, (node.val, pos, node))
        
        return dummy.next
                
                    

