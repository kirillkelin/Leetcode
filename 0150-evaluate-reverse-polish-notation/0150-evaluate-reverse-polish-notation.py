class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "*", "/"]

        for val in tokens:
            if val not in operands:
                stack.append(int(val))
            elif val == "+":
                value_1, value_2 = stack.pop(), stack.pop()
                stack.append(value_2 + value_1)
            elif val == "-":
                value_1, value_2 = stack.pop(), stack.pop()
                stack.append(value_2 - value_1)
            elif val == "*":
                value_1, value_2 = stack.pop(), stack.pop()
                stack.append(value_2 * value_1)
            elif val == "/":
                value_1, value_2 = stack.pop(), stack.pop()
                stack.append(int(value_2 / value_1))

        return stack.pop()