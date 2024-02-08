class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        result = []
        dct_s = {i: 0 for i in range(26)}
        dct_p = {i: 0 for i in range(26)}

        for i in range(len(p)):
            dct_p[ord(p[i]) - ord("a")] += 1
            dct_s[ord(s[i]) - ord("a")] += 1

        left = 0
        # matches = 0
        for right in range(len(p), len(s) + 1):
            # if matches == len(p):
            #     result.append(left)
            #     left = right
            if dct_s == dct_p:
                result.append(left)
            
            if right != len(s):
                dct_s[ord(s[right]) - ord("a")] += 1
                dct_s[ord(s[left]) - ord("a")] -= 1
                left += 1
            
        return result