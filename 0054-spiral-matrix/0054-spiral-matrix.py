class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        ans = []
        while top <= bottom and left <= right:
            # left to right (top row)
            for j in range(left,right+1):
                # print('first',top,j,matrix[top][j])
                ans.append(matrix[top][j])
            top += 1
            # top to bottom ( right col)
            for i in range(top,bottom+1):
                # print('second',i,right, matrix[i][right])
                ans.append(matrix[i][right])
            right -= 1
            # check
            if top > bottom or left > right:
                break
            # right to left ( bottom row)
            for j in range(right,left-1,-1):
                # print('third',bottom,j, matrix[bottom][j])
                ans.append(matrix[bottom][j])
            bottom -= 1
            # bottom to top ()
            for i in range(bottom,top-1,-1):
                # print('forth',i,left, matrix[i][left])
                ans.append(matrix[i][left])
            left += 1
        return ans