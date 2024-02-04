# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countNodes(root, root.val) 


    def countNodes(self, root, max_val):
        k = 0
        if root:
            k = self.countNodes(root.left, max(max_val, root.val)) + self.countNodes(root.right, max(max_val, root.val))
            if root.val >= max_val:
                k += 1
            return k

        return 0

            
