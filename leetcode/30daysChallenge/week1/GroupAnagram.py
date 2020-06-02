# Given an array of strings, group anagrams together.

# Inpu[pop[]t: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


class Solution:
# 	Runtime: 116 ms
# Memory Usage: 18.3 MB
# beats 56.18% that time
	def groupAnagrams(self, strs):
		# strs = sorted(strs)
		# print(strs)
		adict = {}
		result = []
		for i, s in enumerate(strs):
			s = tuple(sorted(list(s)))
			if s not in adict:
				adict[s] = [i]
			else:
				adict[s].append(i)

		for v in adict.values():
			result.append(list(map(lambda x: strs[x], v)))
		return result


class Solution_2:

		def groupAnagrams(self, strs):
			dict = {}
			for word in strs:
				sortedWord = "".join(sorted(word))
				print(sortedWord)
				if sortedWord not in dict:
					dict[sortedWord] = [word]
				else:
					dict[sortedWord].append(word)
			return list(dict.values())



if __name__ == "__main__":
	strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
	print(Solution_2().groupAnagrams(strs))
