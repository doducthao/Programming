# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5 

# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
# 	# super().__init__()

#     def diameterOfBinaryTree(self, root):
#     	return len(root)-1
    	
class Solution:
    def path_length(self, root):
        if root:
            left_path = self.path_length(root.left)
            right_path = self.path_length(root.right)
            path = left_path + right_path
            if path > self.diameter:
                self.diameter = path    
            return max(left_path, right_path)+1
        return 0
        
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.path_length(root)
        return self.diameter



class Solution_2:
    def diameterOfBinaryTree(self, root):
        self.res = 1
        
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.res = max(self.res, left+right+1)
            return(max(left, right)+1)
        
        depth(root)
        return self.res-1



if __name__ == "__main__":
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)

	print(Solution_2().diameterOfBinaryTree(root))

