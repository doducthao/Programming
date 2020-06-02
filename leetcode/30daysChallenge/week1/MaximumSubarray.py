# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
	def maxSubArray(self, nums):
		list_sums = {}
		l = len(nums)
		for i in range(l):
			for j in range(i+1,l+1):
				# print(nums[i:j])
				print(nums[i:j])
				list_sums[str(nums[i:j])] = sum(nums[i:j])
		for k, v in list_sums.items():
			if v == max(list_sums.values()):
				return k, v

class Solution_2:
	def maxSubArray(self, nums):
		list_sums = {}
		l = len(nums)
		for i in range(l):
			for j in range(i+1,l+1):
				# print(nums[i:j])
				list_sums[str(nums[i:j])] = sum(nums[i:j])
		return max(list_sums.values())
		
class Solution_3:
	def maxSubArray(self, nums):
		list_sums = {}
		l = len(nums)
		for i in range(l):
			j = 0
			while j < l:
				# print(j)
				j += 1
				if j > i:
					print(nums[i:j])
					list_sums[str(nums[i:j])] = sum(nums[i:j])
		return max(list_sums.values())
				
class Solution_4:
	# Runtime: 76 ms
	# Memory Usage: 14.7 MB
	def maxSubArray(self, nums):
		total_sum = max_sum = nums[0]

		for i in nums[1:]:
			# print(i)
			total_sum = max(i, total_sum + i)
			# print(total_sum)
			max_sum = max(max_sum, total_sum)
			# print(max_sum)
			# print("\n")
		return max_sum	

class Solution_5:
	# Runtime: 124 ms
# Memory Usage: 14.6 MB
    def maxSubArray(self, nums):
            ans = [nums[0]]
            for i in range(1, len(nums)):
                ans.append(max(ans[-1]+nums[i], nums[i]))
            return max(ans)

class best_Solution:
	# Runtime: 76 ms
	# Memory Usage: 14.5 MB
    def maxSubArray(self, nums: List[int]) -> int:
        max_seq = nums[0]
        curr_sum = nums[0]
        for num in nums[1:]:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num
            if curr_sum > max_seq:
                max_seq = curr_sum
        return max_seq



if __name__=="__main__":
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print(best_Solution().maxSubArray(nums))

	



