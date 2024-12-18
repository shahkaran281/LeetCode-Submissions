from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = Counter()
        n = len(s)
        ans = 0
        
        for i in range(n):
            letters = set()  
            for size in range(minSize, maxSize + 1):
                if i + size > n:
                    break
                
                word = s[i:i + size]
                letters.update(word)
                
                if len(letters) <= maxLetters:
                    count[word] += 1
                    ans = max(ans, count[word])
                else:
                    break  
        return ans
