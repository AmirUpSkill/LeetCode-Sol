# Range Sum Query - Immutable

In this problem, we have an array of integers. For this array, we need to handle multiple queries of this type:

1. Calculate the sum of the elements in `nums` between the indices “left” and “right” (inclusive).

Where `left ≤ right`.

Our goal is to implement the `NumArray` class as follows:

- `NumArray(int[] nums)`: Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)`: Returns the sum of the elements in `nums` between indices `left` and `right`, inclusive (i.e., `nums[left] + nums[left + 1] + ... + nums[right]`).

## Objective

The objective is to implement a function that computes the sum between two bounds, `left` and `right` (inclusive).

## Implementation

This should be implemented by creating a class called `NumArray`.

1. **Initialize the class**: Start by implementing the `__init__` method, which will initialize the array `nums`.

    ```python
    self.nums = nums
    ```

2. **Implement the logic to compute the sum efficiently between two bounds**, `left` and `right`.

### Pattern

This problem can be solved by applying the prefix sum pattern in two main steps:

- **Step 1**: Preprocess the array to create a new array called `prefix_sum`, where each element at index `i` stores the sum of all elements in `nums` up to that index.
- **Step 2**: For each query, use the `left` and `right` indices to compute the sum by leveraging the prefix sum array.

Finally, return the result.

## Example

Given the input array `[-2, 0, 3, -5, 2, -1]`, we create the prefix sum array `[-2, -2, 1, -4, -2, -3]`.

- Edge case if `left = 0`: Just return `prefix[right]`.
- Case `left = 0` and `right = 2`: We just return `1`.
- Edge case if `left = 2` and `right = 5`: We need to handle this correctly.

## Pseudocode

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * len(nums)
        if len(nums) > 0:
            self.prefix_sum[0] = nums[0]
            for i in range(1, len(nums)):
                self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left-1]
