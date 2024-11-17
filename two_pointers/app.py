class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 1):
            left = i + 1
            right = n - 1
            
            while left < right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] >= lower:
                    right = mid
                else:
                    left = mid + 1
            
            start = left if left < n and nums[i] + nums[left] >= lower else n
            
            left = i + 1
            right = n - 1
            
            while left < right:
                mid = (left + right + 1) // 2
                if nums[i] + nums[mid] <= upper:
                    left = mid
                else:
                    right = mid - 1
            
            end = right if right >= 0 and nums[i] + nums[right] <= upper else i
            
            if start <= end:
                count += end - start + 1
                
        return count
