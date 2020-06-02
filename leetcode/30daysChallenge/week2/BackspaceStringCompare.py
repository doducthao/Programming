# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:

# Can you solve it in O(N) time and O(1) space?
import itertools

class Solution:
# 	Runtime: 44 ms
# Memory Usage: 13.8 MB
	def backspaceCompare(self, S, T):
		S, T = list(S.lower()), list(T.lower())
		i = 0
		while i < len(S):
			if S[0] == "#":
				S.pop(0)
				i = 0
				# print(i, S)
			elif S[i] == "#" and i != 0:
				S.pop(i-1)
				S.pop(i-1)
				i = 0
				# print(i, S)
			i += 1 

		j = 0
		while j < len(T):
			if T[0] == "#":
				T.pop(0)
				j = 0
				# print(j, T)
			elif T[j] == "#" and j != 0:
				T.pop(j-1)
				T.pop(j-1)
				j = 0
				# print(j, T)
			j += 1 

		return "".join(S) == "".join(T)

class Solution_2(object):

# Runtime: 32 ms
# Memory Usage: 14.1 MB
	def backspaceCompare(self, S, T):
		def build(S):
			ans = []
			for c in S:
				if c != '#':
					ans.append(c)
				elif ans:
					ans.pop()
			return "".join(ans)
		return build(S) == build(T)

class Solution_3(object):
# 	Runtime: 24 ms
# Memory Usage: 13.7 MB
	def backspaceCompare(self, S, T):
		def F(S):
			skip = 0
			for x in reversed(S):
				if x == '#':
					skip += 1
				elif skip:
					skip -= 1
				else:
					print(x)
					yield x

		return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))




if __name__ == "__main__":
	S, T = "ab##", "ad#c"
	# S, T = "ab##", "c#d#"
	# S, T= "a##c", "#a#c"
	# S, T = "a#c", "b"
	# S, T = "bxj##tw", "bxj###tw"


	



	print(Solution_3().backspaceCompare(S,T))