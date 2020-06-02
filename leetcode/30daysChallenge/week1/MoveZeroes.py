# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


class Solution:
	# runtime: 400ms
	# memory usage: 15.2 mb
	def moveZeroes(self, nums):
		for n in nums:
			if n==0:
				nums.remove(n)
				nums.append(n)
				# print(nums)
		return nums

class Solution_2:
	# runtime: 228ms
	# memory usage: 15.2 mb
	def moveZeroes(self, nums):
		"""
		Do not return anything, modify nums in-place instead.
		"""
		for n in nums:
			if n == 0:
				nums.append(nums.pop(nums.index(n)))
		return nums

class best_Solution:
	def moveZeroes(self, nums):
		slow = fast = 0
		while fast < len(nums):
			print(nums[fast])
			print(nums[slow])
			print(nums)
			
			if nums[fast] != 0:
				# print(nums[fast])
				nums[slow], nums[fast] = nums[fast], nums[slow]

		# wait while we find a non-zero element to
			# switch with you
			if nums[slow] != 0:
				# print(nums[slow])
				slow += 1
			# keep going
			fast += 1
			print(nums)
			print("\n")
		return nums

if __name__ == "__main__":
	nums = [0,1,0,3,12]
	print(best_Solution().moveZeroes(nums))