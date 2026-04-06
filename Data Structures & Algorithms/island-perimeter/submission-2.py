
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    peri =  self.dfs(grid, i, j)
                    break

        return peri

    def dfs(self, grid:List[List[int]], i:int, j:int) -> int:
        if i >= len(grid) or i < 0 or  j >= len(grid[0]) or  j < 0:
            return 1
        if grid[i][j] == 0 :
            return 1
        if grid[i][j] == 2:
            return 0

        grid[i][j] = 2
        return (
            self.dfs(grid, i-1, j) + self.dfs(grid, i, j -1) + self.dfs(grid, i+1, j) + self.dfs(grid, i, j+1) 
        )

        



