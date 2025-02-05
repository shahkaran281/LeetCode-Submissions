from heapq import heapify, heappop, heappush

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.added = set()  
        self.next_num = 1   

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heappop(self.heap)
            self.added.remove(smallest)  
        else:
            smallest = self.next_num
            self.next_num += 1
        
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.added:
            heappush(self.heap, num)
            self.added.add(num)
            
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)