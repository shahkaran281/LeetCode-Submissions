class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        limit = pow(2,k)
        val = 0
        visited = set()
        if len(s) < k:
            return False
        for i in range(k-1):
            val = val*2 + int(s[i])
        # print("Limit:", limit, "Val:",val)
        i = k-1
        while i < len(s):
            val = val*2 + int(s[i])
            # print(val)
            if val < limit:
                visited.add(val)
            if len(visited) == limit:
                return True
            i+=1
            val = val %(limit/2)
        return False
        