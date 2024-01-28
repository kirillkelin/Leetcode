class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct = {}
        left = 0
        max_substring = 0
        result = 0
        for i in range(len(s)):
            dct[s[i]] = dct.get(s[i], 0) + 1
            max_substring = max(max_substring, dct[s[i]])

            if (i - left + 1) - max_substring > k:
                dct[s[left]] -= 1
                left += 1
                
            result = max(result, i - left + 1)
        
        return result