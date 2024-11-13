class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        nums.sort()
        hash_map={num: i for i , num in enumerate(nums)}
        for i , num in enumerate(nums):
            if num*2 in hash_map and hash_map[num*2]!=i:
                return True
        return False 