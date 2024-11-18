from typing import List

class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l,r=0,1
        n=len(nums)
        max_profit=0
        while l < n and r < n : 
            diff=nums[r]-nums[l]
            if diff < 0:
                l+=r
                r=l+1
            else:
                max_profit=max(max_profit,diff)
                r+=1
        return max_profit
