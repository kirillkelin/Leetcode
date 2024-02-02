# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0, True

            left_deep, is_left_balanced = helper(root.left)
            right_deep, is_right_balanced = helper(root.right)

            if is_left_balanced and is_right_balanced and abs(left_deep - right_deep) < 2:
                return 1 + max(left_deep, right_deep), True
        
            return 0, False

        return helper(root)[1]
