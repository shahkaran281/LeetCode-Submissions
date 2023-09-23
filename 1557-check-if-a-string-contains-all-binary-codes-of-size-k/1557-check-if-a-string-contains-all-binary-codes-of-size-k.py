class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        limit = 1 << k
        val = 0
        visited = set()
        for i in range(k-1):
            val = val*2 + int(s[i])
        i = k-1
        while i < len(s):
            val = val*2 + int(s[i])
            visited.add(val)
            if len(visited) == limit:
                return True
            i+=1
            val = val %(limit/2)
        return False
        