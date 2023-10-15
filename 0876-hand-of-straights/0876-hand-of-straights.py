from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], grpSize: int) -> bool:
        if len(hand) % grpSize != 0:
            return False
        count = Counter(hand)
        while len(count)!=0:
            mini = min(count)
            count[mini]-=1
            if count[mini] == 0:
                del count[mini]
            size = 1
            val = mini + 1
            while len(count)!=0 and size < grpSize:
                if val in count:
                    count[val]-=1
                    if count[val] == 0:
                        del count[val]
                    val+=1
                    size+=1
                else:
                    return False
        return True        
        