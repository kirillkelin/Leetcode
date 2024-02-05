class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        result = 0
        while left < len(chars):
            letter = chars[left]
            count = 0
            while left < len(chars) and chars[left] == letter:
                count += 1
                left += 1

            chars[result] = letter
            result += 1
            if count > 1:
                for char in str(count):
                    chars[result] = char
                    result += 1
        
        return result
            