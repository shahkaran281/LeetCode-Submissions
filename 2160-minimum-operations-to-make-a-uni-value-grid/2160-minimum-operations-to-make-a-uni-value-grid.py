class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = [num for row in grid for num in row]
        
        remainder = flattened[0] % x
        for num in flattened:
            if num % x != remainder:
                return -1
        flattened.sort()
        
        median = flattened[len(flattened) // 2]
        
        def calc_cost(target):
            cost = 0
            for num in flattened:
                if abs(num - target) % x != 0:
                    return float('inf')  
                cost += abs(num - target) // x
            return cost
        
        return calc_cost(median)
