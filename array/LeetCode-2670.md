# Find the Distinct Difference Array

## Problem Statement
You are given a 0-indexed array `nums` of length `n`. The task is to compute the "distinct difference array" such that for each index `i` in `nums`, the value at index `i` is defined as:

\[ \text{diff}[i] = \text{suffix}[i] - \text{prefix}[i] \]

where:
- `prefix[i]` is the number of distinct elements in the prefix of `nums` from `0` to `i`.
- `suffix[i]` is the number of distinct elements in the suffix of `nums` from `i+1` to `n-1`.

## Input and Output
- **Input**: `List[int]` (e.g., `nums = [3, 2, 3, 4, 2]`)
- **Output**: `List[int]` (the distinct difference array)

## Example
Let's go through an example with `nums = [3, 2, 3, 4, 2]`:

1. **Compute Prefix Distinct Counts**:
   - For `i = 0`: Prefix = `[3]`, Distinct elements in prefix = `1`
   - For `i = 1`: Prefix = `[3, 2]`, Distinct elements in prefix = `2`
   - For `i = 2`: Prefix = `[3, 2, 3]`, Distinct elements in prefix = `2`
   - For `i = 3`: Prefix = `[3, 2, 3, 4]`, Distinct elements in prefix = `3`
   - For `i = 4`: Prefix = `[3, 2, 3, 4, 2]`, Distinct elements in prefix = `3`

   The prefix distinct counts are: `[1, 2, 2, 3, 3]`

2. **Compute Suffix Distinct Counts**:
   - For `i = 4` (no suffix): Distinct elements in suffix = `0`
   - For `i = 3`: Suffix = `[2]`, Distinct elements in suffix = `1`
   - For `i = 2`: Suffix = `[4, 2]`, Distinct elements in suffix = `2`
   - For `i = 1`: Suffix = `[3, 4, 2]`, Distinct elements in suffix = `3`
   - For `i = 0`: Suffix = `[2, 3, 4, 2]`, Distinct elements in suffix = `3`

   The suffix distinct counts are: `[3, 3, 2, 1, 0]`

3. **Compute Distinct Difference Array**:
   - For `i = 0`: `diff[0] = suffix[0] - prefix[0] = 3 - 1 = 2`
   - For `i = 1`: `diff[1] = suffix[1] - prefix[1] = 3 - 2 = 1`
   - For `i = 2`: `diff[2] = suffix[2] - prefix[2] = 2 - 2 = 0`
   - For `i = 3`: `diff[3] = suffix[3] - prefix[3] = 1 - 3 = -2`
   - For `i = 4`: `diff[4] = suffix[4] - prefix[4] = 0 - 3 = -3`

## Solution
Here's the Python code to solve the "Find the Distinct Difference Array" problem:

```python
from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            postfix_val = len(set(nums[i+1:]))
            prefix_val = len(set(nums[:i+1]))
            result[i] = postfix_val - prefix_val

        return result
