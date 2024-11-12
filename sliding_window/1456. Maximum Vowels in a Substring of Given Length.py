class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current_count = 0
        
        # Count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        count = max(count, current_count)
        
        # Slide the window across the string
        for i in range(k, n):
            if s[i-k] in vowels:
                current_count -= 1  # Remove the vowel going out of the window
            if s[i] in vowels:
                current_count += 1  # Add the new vowel coming into the window
            count = max(count, current_count)  # Update the maximum count
        
        return count 