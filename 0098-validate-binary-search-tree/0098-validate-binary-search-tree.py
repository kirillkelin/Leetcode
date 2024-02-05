# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float("-inf"), float("inf"))


    def check(self, node, left, right):
        if not node:
            return True

        if node.val >= right or node.val <= left:
            return False
        
        return self.check(node.left, left, node.val) and self.check(node.right, node.val, right)


    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
        
    #     if root.left is not None and root.left.val >= root.val:
    #         return False
        
    #     if root.right is not None and root.right.val <= root.val:
    #         return False

    #     return self.isValidLeftBTS(root.left, root.val, float('-inf')) and self.isValidRightBTS(root.right, root.val, float('inf'))

        
    # def isValidLeftBTS(self, root, max_val, min_val):
    #     if not root:
    #         return True
        
    #     if root.left is not None and (root.left.val >= root.val or root.left.val <= min_val):
    #         return False

    #     if root.right is not None and (root.right.val <= root.val or root.right.val >= max_val):
    #         return False

    #     return self.isValidLeftBTS(root.left, root.val, min_val) and self.isValidLeftBTS(root.right, max_val, root.val)

        
    # def isValidRightBTS(self, root, min_val, max_val):
    #     if not root:
    #         return True

    #     if root.left is not None and (root.left.val >= root.val or root.left.val <= min_val):
    #         return False

    #     if root.right is not None and (root.right.val <= root.val or root.right.val >= max_val):
    #         return False

    #     return self.isValidRightBTS(root.left, min_val, root.val) and self.isValidRightBTS(root.right, root.val, max_val)