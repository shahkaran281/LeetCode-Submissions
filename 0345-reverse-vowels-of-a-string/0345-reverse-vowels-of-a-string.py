class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)
        i = 0
        j = len(s) -1
        while i < len(s) and j >=0 and i < j:
            while i < len(s) and s[i] not in vowels:
                i+=1
            while j >=0 and s[j] not in vowels:
                j-=1
            if i < len(s) and j >=0 and i < j:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
        return ''.join(s)