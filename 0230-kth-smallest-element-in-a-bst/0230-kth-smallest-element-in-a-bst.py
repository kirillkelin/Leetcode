# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            count += 1
            current = stack.pop()
            if count == k:
                return current.val
            root = current.right
            




        

