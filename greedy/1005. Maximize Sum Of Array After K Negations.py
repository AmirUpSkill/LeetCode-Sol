from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count_negatives = sum(1 for num in nums if num < 0)
        
        if count_negatives == 0:
            if k % 2 == 1:
                nums[0] = -nums[0]
            return sum(nums)
        
        if k <= count_negatives:
            nums[:k] = [-num for num in nums[:k]]
            return sum(nums)
        else:
            nums[:count_negatives] = [-num for num in nums[:count_negatives]]
            k_remaining = k - count_negatives
            
            if k_remaining % 2 == 1:
                min_index = nums.index(min(nums))
                nums[min_index] = -nums[min_index]
            
            return sum(nums)
