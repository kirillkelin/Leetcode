class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if i == len(temperatures) - 1:
                stack.append(i)
                continue
            elif temperatures[i] >= temperatures[i + 1]:
                stack.pop()
                while stack and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                if stack:
                    result[i] = stack[-1] - i
            else:
                result[i] = 1

            stack.append(i)

        return result