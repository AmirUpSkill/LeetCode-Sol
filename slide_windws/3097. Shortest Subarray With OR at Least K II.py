from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k == 0:
            return -1

        min_length = n + 1
        left = 0
        running_or = 0

        for right in range(n):
            running_or |= nums[right]
            
            while left <= right and running_or >= k:
                min_length = min(min_length, right - left + 1)
                
                if min_length == 1:
                    return 1
                
                new_or = 0
                for i in range(left + 1, right + 1):
                    new_or |= nums[i]
                
                running_or = new_or
                left += 1
        
        return min_length if min_length != n + 1 else -1



