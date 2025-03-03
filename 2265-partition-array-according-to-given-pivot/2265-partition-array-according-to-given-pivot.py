class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_than_pivot = []
        greater_than_pivot = []
        equals = 0
        for number in nums:

            if number < pivot:
                smaller_than_pivot.append(number)

            elif number == pivot:
                equals += 1

            else:
                greater_than_pivot.append(number)
        return smaller_than_pivot + [pivot] * equals + greater_than_pivot