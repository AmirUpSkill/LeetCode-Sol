"""
Common Two Pointer Solution Patterns in Python
This file contains implementations of common two-pointer techniques used in coding problems.
"""

def two_pointers_from_ends(arr):
    """
    Pattern: Two pointers starting from both ends moving towards center
    Useful for: Searching pairs in sorted array, container with most water, etc.
    """
    left = 0
    right = len(arr) - 1
    result = []
    
    while left < right:
        # Process elements at left and right pointers
        current_sum = arr[left] + arr[right]
        
        # Example: Finding pairs that sum to target
        if current_sum == target:
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return result

def two_pointers_same_direction(arr):
    """
    Pattern: Two pointers moving in same direction
    Useful for: Remove duplicates, finding subarrays, etc.
    """
    slow = 0
    
    for fast in range(len(arr)):
        # Process using slow and fast pointers
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1  # Length of array after removing duplicates

def sliding_window(arr):
    """
    Pattern: Sliding window with two pointers
    Useful for: Finding subarrays with certain properties
    """
    left = 0
    window_sum = 0
    max_sum = float('-inf')
    
    for right in range(len(arr)):
        # Add element to window
        window_sum += arr[right]
        
        # Shrink window if condition is violated
        while window_sum > target:
            window_sum -= arr[left]
            left += 1
        
        # Update result
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def fast_slow_pointers(head):
    """
    Pattern: Fast and slow pointers (Floyd's cycle detection)
    Useful for: Detecting cycles in linked list, finding middle element
    """
    if not head or not head.next:
        return None
    
    slow = head
    fast = head
    
    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # Cycle detected
    
    return False  # No cycle

def merge_two_sorted_arrays(arr1, arr2):
    """
    Pattern: Two pointers for merging
    Useful for: Merging sorted arrays/lists
    """
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
