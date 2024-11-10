class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words, filtering out extra spaces
        word_list = s.split()  
        # Reverse the order of words and join them with a single space
        return " ".join(word_list[::-1])  