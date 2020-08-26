import numpy as np 
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.check(grid, i, j)
                    count += 1
        return count

    def check(self, grid, i, j):
        if i<0 or j<0 or i>= len(grid) or j>= len(grid[0]) or grid[i][j] != "1":
            return

        grid[i][j] = "#"
        self.check(grid, i+1, j)
        self.check(grid, i-1, j)
        self.check(grid, i, j+1)
        self.check(grid, i, j-1)

class Solution_2:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    count += 1
                    print(count)
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = '#'
        print(grid)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


if __name__ == "__main__":
    grid = [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]
            ]
    # grid = np.asarray(grid)
    print(grid)
    print(grid[0])
    print(grid[1])
    print(len(grid))
    print("\n")
    
    result = Solution_2().numIslands(grid)
    print(result)