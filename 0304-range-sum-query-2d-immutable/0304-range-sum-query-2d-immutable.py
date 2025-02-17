class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.matrixSum = matrix
        self.colSum = matrix
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                self.matrixSum[i][j] += self.matrixSum[i][j-1]
        for j in range(len(matrix[0])):
            for i in range(1,len(matrix)):
                self.matrixSum[i][j] += self.matrixSum[i-1][j]
        for row in self.matrixSum:
            print(row)
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = self.matrixSum[row2][col2]
        # print('1',self.matrixSum[row2][col2])
        if row1 != 0:
            # print('2', self.matrixSum[row1-1][col2])
            summ -=(self.matrixSum[row1-1][col2]) 
        if col1 != 0:
            # print('3', self.matrixSum[row2][col1-1])
            summ -= self.matrixSum[row2][col1-1]
        if row1 != 0 and col1!= 0:
            # print('4', self.matrixSum[row1-1][col1-1])
            summ += self.matrixSum[row1-1][col1-1]
        return summ
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)