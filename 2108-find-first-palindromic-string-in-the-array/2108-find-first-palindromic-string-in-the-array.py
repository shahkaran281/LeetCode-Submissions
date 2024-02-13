class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = ""
        def isPali(word):
            i = 0
            j = len(word)-1
            while i < j:
                # print(f'i: {i} j:{j}')
                if word[i] != word[j]:
                    return False
                i+=1
                j-=1
            return True
        for word in words:
            if isPali(word):
                res = word
                break
        return res
        