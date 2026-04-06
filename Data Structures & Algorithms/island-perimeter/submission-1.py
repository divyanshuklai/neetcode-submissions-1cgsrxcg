
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
        if grid[i][j] == 0 or grid[i][j] == 2 :
            return 0
        
        grid[i][j] = 2
        peri = 0
        if i > 0 and grid[i-1][j] == 0:
            peri += 1
        else:
            peri += self.dfs(grid, i-1, j)

        if i < len(grid) -1 and grid[i+1][j] == 0:
            peri +=1
        else:
            peri += self.dfs(grid, i+1, j)
        
        if j > 0 and grid[i][j-1] == 0:
            peri+=1
        else:
            peri+= self.dfs(grid, i, j-1)
        
        if j < len(grid[0]) - 1 and grid[i][j+1] == 0:
            peri+=1
        else:
            peri+= self.dfs(grid, i, j+1)
        
        return peri

        



