from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(row,col):
            queue = deque()
            grid[row][col] = "0"

            queue.append((row,col))

            while len(queue) != 0:
                r, c = queue.pop()
                for dx,dy in directions: 
                    if 0 <= r+dx < rows and 0 <= c + dy < cols and grid[r+dx][c+dy] == "1":
                        queue.append((r+dx,c+dy))
                        grid[r+dx][c+dy] = "0"
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i,j)
                    islands += 1

        
        return islands