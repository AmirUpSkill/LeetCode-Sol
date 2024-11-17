class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 3:  # Check if the string is shorter than 3
            return 0
        s = list(s)
        count = 0
        hash_map = Counter(s[:3])
        if len(hash_map) == 3:
            count += 1
        for i in range(3, n):
            hash_map[s[i-3]] -= 1
            if hash_map[s[i-3]] == 0:
                del hash_map[s[i-3]]
            hash_map[s[i]] += 1
            if len(hash_map) == 3:
                count += 1
        return count
