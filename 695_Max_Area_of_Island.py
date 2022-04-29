class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def dfs(i,j):
            nonlocal grid

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0

            maxArea = 1
            grid[i][j] = '#'

            maxArea += dfs(i-1,j)
            maxArea += dfs(i+1,j)
            maxArea += dfs(i, j-1)
            maxArea += dfs(i, j+1)

            return maxArea


        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea




        
