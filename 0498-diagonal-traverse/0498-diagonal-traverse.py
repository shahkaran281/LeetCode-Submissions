class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        num_rows = len(mat)
        num_cols = len(mat[0])
        result = []

        for k in range(num_rows + num_cols - 1):
            temp = []
            row = 0 if k < num_cols else k - num_cols + 1
            col = k if k < num_cols else num_cols - 1

            while row < num_rows and col >= 0:
                temp.append(mat[row][col])
                row += 1
                col -= 1

            if k % 2 == 0:
                result.extend(temp[::-1])
            else:
                result.extend(temp)

        return result