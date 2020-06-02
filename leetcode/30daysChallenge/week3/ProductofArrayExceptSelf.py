# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i]
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)



# class Solution:
#     def productExceptSelf(self, nums):
#     	alist = []
#     	value = 1
#     	for i, x in enumerate(nums):
#     		value *= x
    		
#     	return alist
    		



class Solution:
    def productExceptSelf(self, nums):
         n=len(nums)
         res, left, right = [0]*n, [0]*n,[0]*n
         left[0] = right[n-1] = 1
         print(left)
         print(right)

         for i in range(1,n):
             left[i] = left[i-1]*nums[i-1]
             print(left[i])
         print(left)
         for i in range(n-2,-1,-1):
             right[i] = right[i+1]*nums[i+1]
             print(right[i])
         print(right)
         for i in range(n):
             res[i] = left[i]*right[i]
             print(res[i])
         return res

if __name__ == "__main__":
	nums = [4,2,3,4]
	print(Solution().productExceptSelf(nums))