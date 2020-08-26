# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# for small grid
class Solution:
	def minPathSum(self, grid):

		if not grid:
			return 0

		results = []
		self.results = results
		self.helper(grid, result=0, i=0, j=0)
		return min(self.results)

	def helper(self, grid, result, i, j):
		if i<len(grid) and j<len(grid[0]):
			result += grid[i][j]
			# print("[i,j]: {}, result: {}".format([i,j], result))
			self.helper(grid, result, i, j+1)
			self.helper(grid, result, i+1, j)
			if i == len(grid)-1 and j==len(grid[0])-1:
				self.results.append(result)
				# print("end of path so we stop")
				# print(self.results)

# best solution
class Solution_2:
	def minPathSum(self, grid):
		c = len(grid)
		r = len(grid[0])    
		for i in range(c):
			for j in range(r):
				if i ==0 and j ==0:
					continue
				elif i == 0:
					grid[i][j] += grid[i][j-1]
				elif j == 0:
					grid[i][j] += grid[i-1][j]
				else:
					grid[i][j] += min(grid[i][j-1], grid[i-1][j])              
		return grid[-1][-1]

class Solution_3:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		dp = [0] * n
		for i in range(m):
			dp[0] += grid[i][0]
			for j in range(1, n):
				dp[j] = (min(dp[j], dp[j-1]) or dp[j-1]) + grid[i][j]
		return dp[-1]

if __name__ == "__main__":
	# grid = [[1,3,1,2,8,4],
	# 		[1,5,13,4,5,10],
	# 		[4,5,4,4,2,1]]
	# grid = 	[[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
	# 		 [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
	# 		 [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
	# 		 [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
	# 		 [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
	# 		 [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
	# 		 [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
	# 		 [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
	# 		 [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
	# 		 [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
	# 		 [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
	# 		 [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

	grid = [[1,2,3,4],
			[1,1,2,2],
			[1,1,1,100]]
	# if not grid:
	# 	print(0)
	# print(len(grid), len(grid[0]))

	print(Solution_2().minPathSum(grid))