class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        w_size = 5 + k
        count = 0
        vowels = set("aeiou")
        n = len(word)

        def is_valid(substring):
            vowel_count = {v: 0 for v in vowels}
            consonant_count = 0
            for char in substring:
                if char in vowels:
                    vowel_count[char] += 1
                else:
                    consonant_count += 1
            return all(v > 0 for v in vowel_count.values()) and consonant_count == k

        for i in range(0, n - w_size + 1):
            current_sub_arr = word[i:i + w_size]
            if is_valid(current_sub_arr):
                count += 1

        return count 