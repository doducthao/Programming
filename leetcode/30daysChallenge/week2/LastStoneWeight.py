# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

# Note:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

class Solution:
# 	Runtime: 20 ms
# Memory Usage: 13.8 MB
# beats 98.01 % at that time
    def lastStoneWeight(self, stones):
    	stones = sorted(stones)
    	# print(stones)
    	if len(stones) == 0:
    		return 0
    	if len(stones) == 1:
    		return stones[-1]
    	elif len(stones) > 1:
    		st1, st2 = stones[-2], stones[-1]
    		if st1 == st2:
    			del stones[-2:]
    			return self.lastStoneWeight(stones)
    		elif st1 < st2:
    			del stones[-2:]
    			stones.append(st2-st1)
    			return self.lastStoneWeight(stones)

class Solution_2:
    def lastStoneWeight(self, nums):
        if not nums:
            return 0
        
        elif len(nums) == 1:
            return nums[0]
        
        elif len(nums) == 2:
            return abs(nums[0] - nums[1])
        
        else:
            max1 = max(nums)
            nums.remove(max1)
            max2 = max(nums)
            nums.remove(max2)
        
            if max1 != max2:
                val = abs(max1-max2)
                nums.append(val)

        val = self.lastStoneWeight(nums)
        return val


if __name__ == "__main__":
	stones = [2,7,4,1,8,1]
	# stones = [2,2,2,2,2,2]
	print(Solution().lastStoneWeight(stones))
