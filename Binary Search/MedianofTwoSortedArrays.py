from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        half = (len(nums1) + len(nums2)) // 2
        
        if len(A) > len(B): 
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True: 
            mid1 = l + ((r - l) // 2) # Mid index of smaller array 
            mid2 = half - (mid1 + 1) - 1 # Mid index of larger array 
            
            Aleft = A[mid1] if mid1 >= 0 else -float('infinity')
            Aright = A[mid1 + 1] if mid1 + 1 < len(A) else float('infinity')
            Bleft = B[mid2] if mid2 >= 0 else -float('infinity')
            Bright = B[mid2 + 1] if mid2 + 1 < len(B) else float('infinity')
            
            if Aleft <= Bright and Bleft <= Aright: #partition is correct
                if (len(nums1) + len(nums2)) % 2 == 1: # odd case
                    return min(Aright,Bright)
                else: 
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: 
                r = mid1 - 1 # too many items in partition of A 
            else: 
                l = mid1 + 1 # too little items in partiton of A 
                
        