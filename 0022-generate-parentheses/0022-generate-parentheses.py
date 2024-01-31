class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursive(opened, closed, n):
            if opened == closed == n:
                result.append("".join(stack))
                return 

            if opened < n:
                stack.append("(")
                recursive(opened + 1, closed, n)
                stack.pop()

            if closed < opened:
                stack.append(")")
                recursive(opened, closed + 1, n)
                stack.pop()


        opened = 0
        closed = 0
        stack = []
        result = []

        recursive(0, 0, n)
        return result