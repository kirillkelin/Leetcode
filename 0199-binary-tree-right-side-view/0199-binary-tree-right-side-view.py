# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root

        dq = deque([root])
        result = []

        while dq:
            length = len(dq)
            for i in range(length):
                tmp = dq.popleft()
                if i == length - 1:
                    result.append(tmp.val)

                if tmp.left:
                    dq.append(tmp.left)
                if tmp.right:
                    dq.append(tmp.right)
            

        return result