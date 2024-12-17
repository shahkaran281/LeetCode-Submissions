from heapq import heappop, heappush, heapify
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str: 
        count = Counter(s)

        maxHeap = [(-ord(c),cnt) for c,cnt in count.items()]
        heapify(maxHeap)
        res = []

        while maxHeap:
            char, cnt = heappop(maxHeap)
            char = chr(-char)
            currCount = min(cnt,repeatLimit)
            res.append(char * currCount)
            
            if cnt - currCount > 0 and maxHeap:
                nxtChar, nxtCount = heappop(maxHeap)
                nxtChar  = chr(-nxtChar)
                res.append(nxtChar)
                if nxtCount > 1:
                    heappush(maxHeap, (-ord(nxtChar),nxtCount - 1))
                heappush(maxHeap,(-ord(char), cnt - currCount))

        return ''.join(res)
