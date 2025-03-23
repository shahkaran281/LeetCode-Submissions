class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2
        
        for i in range(n):
            total_cost += costs[i][0]  # City A cost for the first n people
        
        for i in range(n, len(costs)):
            total_cost += costs[i][1]  # City B cost for the remaining people
        
        return total_cost
