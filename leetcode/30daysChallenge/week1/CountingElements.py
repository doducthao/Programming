# Given an integer arr, count element x such that x+1 is also arr
# if there's duplicates in arr, count them seperately

class Solution:
	def Count(self, arr):
		adict = {}
		# add = False
		for x in arr:
			if x not in adict and x+1 in arr:
				adict[x] = 1
			elif x in adict and x+1 in arr:
				adict[x] += 1
		return sum(adict.values())


if __name__ == "__main__":
	arr = [2,2,2,4,4,4,3,-1,2]
	print(Solution().Count(arr))