class Solution:
    def removeStars(self, s: str) -> str:
        """
        LeetCode 2390: Removing Stars From a String
        
        You are given a string s, which contains stars *.
        In one operation, you can:
        - Choose a star in s.
        - Remove the closest non-star character to its left, as well as remove the star itself.
        Return the string after all stars have been removed.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Example:
        Input: s = "leet**cod*e"
        Output: "lecoe"
        Explanation: 
        - The first '*' removes 't' and itself, resulting in "lee*cod*e"
        - The second '*' removes 'e' and itself, resulting in "lecod*e"
        - The third '*' removes 'd' and itself, resulting in "lecoe"
        """
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            if char == '*':
                # If we encounter a star and stack is not empty,
                # remove the last character from stack
                if stack:
                    stack.pop()
            else:
                # Add non-star character to stack
                stack.append(char)
        
        # Join all characters in stack to form the result
        return ''.join(stack)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        "leet**cod*e",
        "erase*****",
        "abc*d*e*f",
        "string***",
        "a*b*c*d"
    ]
    
    for test in test_cases:
        result = solution.removeStars(test)
        print(f"Input: {test}")
        print(f"Output: {result}\n")
