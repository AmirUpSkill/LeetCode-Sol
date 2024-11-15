class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        s = list(s)
        t = list(t)
        i = 0
        j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == n else False

# Here’s the English translation of your notes for the problem "Is Subsequence":
#
# ---
#
# **Problem Statement:**
#
# We are given two strings, `s` and `t`. Our task is to return `True` if `s` is a subsequence of `t`, and `False` otherwise.
#
# **Q: What is a subsequence?**
#
# A subsequence of a string is a new string formed by deleting some (or possibly none) of the characters from the original string without changing the relative positions of the remaining characters.
#
# For example, `"ace"` is a subsequence of `"abcde"`, but `"aec"` is not.
#
# **Q: What is the input and output format?**
#
# - Input: Two strings (`s`, `t`)
# - Output: Boolean (`True` or `False`)
#
# **Q: Can you go through an example?**
#
# Let's take an example where:
#
# - `s = "abc"`
# - `t = "ahbgdc"`
#
# Explanation:
#
# 1. `s` has three characters.
#     - The character `"a"` is at index 0 in `t`.
#     - The character `"b"` is at index 2 in `t`.
#     - The character `"c"` is at index 5 in `t`.
# 2. All characters of `s` appear in `t` in the same relative order.
# 3. Therefore, `s` is a subsequence of `t`, and we return `True`.
#
# **Approach:**
#
# 1. First, we need to check if all characters of `s` are present in `t`.
# 2. Second, we must ensure that the relative order of characters in `s` is maintained in `t`.
#
# ---
#
# Q- fe awll challange ntswer using two pointers and transform t into set (which make the lockup O(1)) not O(n) in array ) can be efficient 
#
# Q- but what about the realtive order can you give me some hints 
#
# Q- before answer the questionn
#
# ---
#
# bahii the mecasime here is simple ? 
#
# we just need two pointers “i” and “j” 
#
# - `s = "abc"`
# - `t = "ahbgdc"`
#
# i intialy —> “a” 
#
# j initialy —> “a” (t) 
#
# next while i < n and j < m : 
#
# we check if s[i]==s[t]:
#
# // move i by one so 
#
# // return True 
#
# j+=1 
#
# return False 
#
# Here’s a formatted version of your notes:
#
# ---
#
# **Q: Can we make this solution efficient?**
#
# Yes! One way to make it efficient is to:
#
# - Use two pointers.
# - Transform `t` into a set, which allows `O(1)` lookups for checking if characters in `s` exist in `t`, rather than `O(n)` lookups in an array.
#
# However, transforming `t` into a set only helps with **existence checks**. This doesn’t guarantee the **relative order**.
#
# **Q: How can we handle the relative order? Any hints?**
#
# Sure, here’s a high-level outline:
#
# 1. Use two pointers: `i` for `s` and `j` for `t`.
# 2. Traverse both strings with these pointers to check if characters in `s` appear in `t` in the correct order.
#
# ---
#
# **Mechanism Explanation (Example):**
#
# Let’s go through an example:
#
# - Given:
#     - `s = "abc"`
#     - `t = "ahbgdc"`
# 1. **Pointer Initialization**:
#     - `i` starts at the beginning of `s` (points to `"a"` in `s`).
#     - `j` starts at the beginning of `t` (points to `"a"` in `t`).
# 2. **Loop with Condition**:
#     
#     While `i < len(s)` and `j < len(t)`:
#     
#     - **Step 1**: Check if `s[i] == t[j]`.
#         - If they match, increment `i` by 1 (move to the next character in `s`).
#     - Increment `j` by 1 each time (always move through `t`).
# 3. **Final Check**:
#     - If `i` reaches the end of `s`, return `True` (indicating that `s` is a subsequence of `t`).
#     - If `j` reaches the end of `t` first, return `False`.
#
# ---
#
# This approach ensures we maintain both **existence** and **relative order**. 