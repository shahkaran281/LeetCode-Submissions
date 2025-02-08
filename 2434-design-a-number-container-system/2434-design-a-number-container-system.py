from heapq import heapify, heappop, heappush
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.container = defaultdict()
        self.indexes = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.container[index] = number
        heappush(self.indexes[number], index)
        # print('Change', index, number)
        # print(self.container)
        # print(self.indexes)

            
    def find(self, number: int) -> int:
        while number in self.indexes and self.container[self.indexes[number][0]] != number:
            heappop(self.indexes[number])
            if len(self.indexes[number]) == 0:
                del self.indexes[number]
                return -1
        if number in self.indexes and len(self.indexes[number]) > 0:
            return self.indexes[number][0]
        else:
            return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)