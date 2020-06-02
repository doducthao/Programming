# Given a non-empty, singly linked list with head node, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Note:

# The number of nodes in the given list will be between 1 and 100

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.


# Definition for singly-linked list.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution(object):
	def middleNode(self, head):
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			# print(slow.val, fast.val)
		return slow

class Solution_2:
	def middleNode(self, head):
		A = [head]
		while A[-1].next:
			A.append(A[-1])
		return A[len(A)/2]


if __name__ == "__main__":
	one = ListNode(1)
	two = ListNode(2)
	three = ListNode(3)
	four = ListNode(4)
	five = ListNode(5)
	six = ListNode(6)
	one.next = two
	two.next = three
	three.next = four
	four.next = five
	five.next = six

	print(Solution().middleNode(one).val)
