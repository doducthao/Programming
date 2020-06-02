# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Note: The length of the given binary array will not exceed 50,000.



class Solution_2:
	def findMaxLength(self, nums):
		d = {}
		curr = 0
		ans = 0
		for i in range(len(nums)):
			if nums[i]==1:
				curr += 1
			else:
				curr -= 1
			
			if curr==0:
				ans = max(ans, i+1)
			
			if curr in d:
				ans = max(ans, i-d[curr])
			else:
				d[curr] = i
		
		return ans

class Solution_3:
	def findMaxLength(self, nums):
		res=0
		tem={0:-1}
		count=0
		length=0
		for i in range(len(nums)):
			if nums[i]==0:
				count+=1
			if nums[i]==1:
				count-=1
			if count in tem:
				length=i-tem[count]
			if count not in tem:
				tem[count]=i            
			res=max(res,length)

		return res

class Solution_4:
	def findMaxLength(self, nums):
		# dictionary
		prefixSum = {0: -1}
		total = 0
		maxlength = 0
		
		for index, value in enumerate(nums):
			print(index, value)
			if value == 0:
				total -= 1
				print("value=0", total)
			else:
				total += 1
				print("value=1", total)
			if total not in prefixSum.keys():
				prefixSum[total] = index
				print("new total", prefixSum)
			else:
				maxlength = max(maxlength, index-prefixSum[total])
				print("maxlength", maxlength)
		print("\n")
		return maxlength



if __name__ == "__main__":
	nums = [0,0,0,1,0,1,0,1,1,1]
	# nums = [0,1]
	print(Solution().findMaxLength(nums))