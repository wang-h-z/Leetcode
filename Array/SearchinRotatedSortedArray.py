from typing import List

# O(logn) time, O(1) space
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search for actual start of array
        left, right = 0, len(nums) - 1
        while left < right: 
            mid = left + ((right - left)) // 2
            
            if nums[mid] > nums[right]: 
                left = mid + 1
            else: 
                right = mid

        pivot = left
        left = 0
        right = len(nums) - 1
        # determine which sorted portion i should search in
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else: 
            right = pivot
        
        # normal binary search
        while left <= right: 
            mid = left + ((right - left)) // 2
                
            if nums[mid] == target: 
                return mid 
            if nums[mid] > target: 
                right = mid - 1
            if nums[mid] < target: 
                left = mid + 1
        
        return -1


print(Solution().search([4,5,6,7,0,1,2], 0))
# Alternative Solution 
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while (left <= right): 
            mid = left + ((right - left) // 2) 
            if nums[mid] == target: 
                return mid 
            
            if nums[left] <= nums[mid]:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[left]: 
                    left = mid + 1
                else: 
                    right = mid - 1
    
            else: 
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[right]:
                    right = mid - 1
                else: 
                    left = mid + 1 
                    
        return -1
"""
