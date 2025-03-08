class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        blacks = 0
        for i in range(k-1):
            blacks += (blocks[i] == 'W') 
        for i in range(k-1,len(blocks)):
            blacks += (blocks[i] == 'W') 
            ans = min(ans, blacks)
            blacks -= (blocks[i-k+1] == 'W')
        return ans