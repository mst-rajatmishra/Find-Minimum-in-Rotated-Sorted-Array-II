from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[right]:
                right = mid  # Minimum is in the left part
            elif nums[mid] > nums[right]:
                left = mid + 1  # Minimum is in the right part
            else:
                right -= 1  # Skip the duplicate
        
        return nums[left]

# Example usage:
# sol = Solution()
# print(sol.findMin([1, 3, 5]))         # Output: 1
# print(sol.findMin([2, 2, 2, 0, 1]))   # Output: 0
