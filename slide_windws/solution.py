from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Handle edge case where k <= 1
        if k <= 1:
            return 0
        
        n = len(nums)
        left = 0
        product = 1
        count = 0
        
        # Iterate through the array using right pointer
        for right in range(n):
            # Include the current element in product
            product *= nums[right]
            
            # Shrink window while product >= k
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            
            # Add count of valid subarrays ending at right
            count += right - left + 1
        
        return count 