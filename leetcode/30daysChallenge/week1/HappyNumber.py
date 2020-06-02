# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.


class Solution(object):
	# Runtime: 36 ms
	# Memory Usage: 13.8 MB
	def isHappy(self, num):
		while 1:
			if self.solve(num) in [0,2,4,6,8]:
				return 0
			elif self.solve(num) == 1:
				return 1
			else:
				num = self.solve(num)
		return 1


	def solve(self, num):
		result = 0
		while num > 0:
			result += (num%10)**2
			num = (num-(num%10)) // 10
		return result


class Solution_2:
	# Runtime: 36 ms
	# Memory Usage: 13.8 MB
	def isHappy(self, num):
		return self.solve(num, {})

	def solve(self, num, visited):
		num =  sum([x**2 for x in l])
		if num == 1:
			return 1
		if num in visited:
			return 0
		visited[num] = 1
		l = list(str(num))
		l = list(map(int, l))
		return self.solve(num, visited)

class Solution_3:
	def isHappy(self, num, past):
		num = sum(int(i)**2 for i in str(num))
		if num == 1:
			return 1
		elif num in past:
			return 0
		else:
			past.add(num)
			return self.isHappy(num, past)



if __name__ == "__main__":
	num = 1111111
	print(Solution_3().isHappy(num, past = set()))

