# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        deep_left = self.maxDepth(root.left)
        deep_right = self.maxDepth(root.right)

        max_deep = max(deep_left, deep_right)
        return max_deep + 1