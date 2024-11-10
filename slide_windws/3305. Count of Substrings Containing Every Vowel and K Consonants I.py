class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        min_size = 5 + k
        count = 0
        
        for w_size in range(min_size, n + 1):
            for i in range(0, n - w_size + 1):
                current_sub_arr = word[i:i + w_size]
                
                vowel_count = {v: 0 for v in vowels}
                consonant_count = 0
                for char in current_sub_arr:
                    if char in vowels:
                        vowel_count[char] += 1
                    else:
                        consonant_count += 1
                if all(v > 0 for v in vowel_count.values()) and consonant_count == k:
                    count += 1
        return count