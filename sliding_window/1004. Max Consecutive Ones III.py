from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0                # Left pointer of the sliding window
        zero_count = 0          # Count of 0's in the current window
        max_length = 0          # Tracks the maximum length of 1's sequence

        for right in range(len(nums)):
            # If we encounter a 0, we increment the zero_count
            if nums[right] == 0:
                zero_count += 1

            # If zero_count exceeds k, we need to shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1  # Decrease zero count as we move left past a 0
                left += 1  # Move left pointer to the right

            # Update max_length with the current window size
            max_length = max(max_length, right - left + 1)

        return max_length 