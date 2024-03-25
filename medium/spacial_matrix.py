class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []

        top = 0
        bottom = len(matrix) - 1
        
        left = 0
        right = len(matrix[0]) - 1

        dydx = 0 
        while top <= bottom and left <= right:
            if dydx == 0:
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                top +=1 
                dydx = 1
            elif dydx == 1:
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right -= 1
                dydx = 2
            elif dydx == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                dydx = 3
            elif dydx == 3:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
                dydx = 0
        return res
