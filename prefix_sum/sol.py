def pivotIndex(nums: list[int]) -> int:
    n = len(nums)
    prefix_sum = []
    postfix_sum = []
    a = 0
    b = 0
    
    for i in range(n):
        a += nums[i]
        prefix_sum.append(a)
    
    for i in range(n-1, -1, -1):
        b += nums[i]
        postfix_sum.insert(0, b)
    
    for i in range(n):
        left_sum = prefix_sum[i] - nums[i]
        right_sum = postfix_sum[i] - nums[i]
        if left_sum == right_sum:
            return i
    
    return -1
