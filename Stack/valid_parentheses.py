class Solution:
    def isValid(self, s: str) -> bool:
        """
        LeetCode 20: Valid Parentheses
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        # Dictionary to map closing brackets to their corresponding opening brackets
        brackets = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            # If it's an opening bracket, push to stack
            if char not in brackets:
                stack.append(char)
            # If it's a closing bracket
            else:
                # Check if stack is empty or top element doesn't match
                if not stack or stack.pop() != brackets[char]:
                    return False
        
        # String is valid only if stack is empty at the end
        return len(stack) == 0

# Test cases
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}"
    ]
    
    for test in test_cases:
        result = solution.isValid(test)
        print(f"Input: {test}")
        print(f"Output: {result}\n")
