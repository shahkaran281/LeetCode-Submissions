from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], grpSize: int) -> bool:
        # Approach #1 : Using Hash Table [ dict / Counter ]
        # if len(hand) % grpSize != 0:
        #     return False
        # count = Counter(hand)
        # while len(count)!=0:
        #     mini = min(count)
        #     count[mini]-=1
        #     if count[mini] == 0:
        #         del count[mini]
        #     size = 1
        #     val = mini + 1
        #     while len(count)!=0 and size < grpSize:
        #         if val in count:
        #             count[val]-=1
        #             if count[val] == 0:
        #                 del count[val]
        #             val+=1
        #             size+=1
        #         else:
        #             return False
        # return True      

        # Approach #2: Iterative Soln
        hand.sort()
        if len(hand) % grpSize != 0:
            return False
        i = 1
        start = 0
        size = 1
        n = len(hand)
        while i < n:
            size = 1
            val = hand[start] + 1
            hand[start] = -1
            while i < n and size < grpSize:
                while i < n and hand[i] != val:
                    i += 1
                if i == n:
                    return False
                size += 1
                hand[i] = -1
                val = val + 1
            if i == n:
                break
            while start < n and hand[start] == -1:
                start += 1
            i = start + 1
        return size == grpSize
        