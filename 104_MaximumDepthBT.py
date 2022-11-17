# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def solve(tree, depth=0):
            if tree is None:
                return depth
            return max(solve(tree.right, depth+1), solve(tree.left, depth+1))
        return solve(root)
