# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self, node_1, node_2):
        if node_1 is None and node_2 is None:
            return True

        if node_1 is None or node_2 is None:
            return False

        if node_1.val != node_2.val:
            return False

        return self.sameTree(node_1.left, node_2.left) and self.sameTree(node_1.right, node_2.right)