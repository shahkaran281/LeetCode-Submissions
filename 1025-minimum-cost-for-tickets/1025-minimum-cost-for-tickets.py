class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        DP = [0] * (days[-1]+1)
        i = 0
        for j in range(1,days[-1]+1):
            print(days[i], j!= days[i])
            if j != days[i]:
                DP[j] = DP[j-1]
            else:
                DP[j] = DP[j-1] + min(costs[0], min(costs[1],costs[2]))
                if j - 7 >= 0:
                    DP[j] = min(DP[j],DP[j-7]+min(costs[1],costs[2]))
                else:
                    DP[j] = min(DP[j],costs[1])
                if j - 30 >= 0:
                    DP[j] = min(DP[j], DP[j-30] + costs[2])
                else:
                    DP[j] = min(DP[j],costs[2])
                i+=1
            print(f"j:{j} cost: {DP[j]}")
        return DP[-1]
        