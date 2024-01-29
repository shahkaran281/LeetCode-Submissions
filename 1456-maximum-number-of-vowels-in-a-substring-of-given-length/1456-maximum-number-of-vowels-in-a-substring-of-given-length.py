class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels =  {'a','i','o','u','e'}
        res = 0
        currRes = 0
        for i in range(len(s)):
            if i - k >= 0:
                if s[i-k] in vowels:
                    currRes -= 1
                # print(f'LAST Position : {i-k} val: {s[i-k]} curr: {currRes}')
            if s[i] in vowels:
                currRes +=1
            res = max(res, currRes)
            # print(f'i: {i} s[i]: {s[i]} curr : {currRes} last : {i-k}')


                
        return res
        
        