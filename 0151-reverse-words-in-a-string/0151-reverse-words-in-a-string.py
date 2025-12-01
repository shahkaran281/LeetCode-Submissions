class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s.split())[::-1]
        print(arr)
        return " ".join(arr)