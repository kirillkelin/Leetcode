class Solution:
    def isValid(self, s: str) -> bool:
        dct = {")": "(", "}": "{", "]": "["}
        stack = []
            
        for char in s:
            if char == '(' or char == "[" or char == "{":
                stack.append(char)
            elif len(stack) and dct[char] == stack[len(stack)-1]:
                stack.pop()
            else:
                stack.append(char)
                break
                         
        return len(stack) == 0
            
        

        
            
        

        