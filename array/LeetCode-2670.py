class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            postfix_val = len(set(nums[i+1:]))
            prefix_val = len(set(nums[:i+1]))
            result[i] = prefix_val - postfix_val 
        
        return result
            