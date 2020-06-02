class Solution:
    def singleNumber(self, nums):
        first = nums[0]
        for num in nums[1:]:
            first = first ^ num 
            # a^0 --> a, a^a --> 0, (a^b^c) --> (a^(b^c)), (b^a^a) --> b^0 = b
        return first

class Solution_2:
	def singleNumber(self, nums):
		adict = {}
		for num in nums:
			if num not in adict:
				adict[num] = 1
			else:
				adict[num] += 1
		for k, v in adict.items():
			if v == 1:
				return k

import collections
 
class Solution_3:
	def singleNumber(self, nums):
		adict = collections.defaultdict(int)
		for num in  nums:
			adict[num] += 1
		for item in adict:
			if adict[item] == 1:
				return item











if __name__ == "__main__":
	nums = [4,1,2,2,1]
	print(Solution().singleNumber(nums))
	print(Solution_2().singleNumber(nums))
	print(Solution_3().singleNumber(nums))
