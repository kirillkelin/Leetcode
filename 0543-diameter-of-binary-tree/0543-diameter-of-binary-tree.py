# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_edges_inside, max_edges = self.maxDeep(root)

        return max(max_edges_inside, max_edges - 1)

    def maxDeep(self, root):
        if not root:
            return 0, 0

        current_edges_left, current_length_left = self.maxDeep(root.left)
        current_edges_right, current_length_right = self.maxDeep(root.right)

        return max(current_length_left + current_length_right, current_edges_left, current_edges_right), max(
            current_length_left, current_length_right) + 1


