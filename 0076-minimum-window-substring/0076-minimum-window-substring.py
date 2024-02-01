class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        dct_t = {}
        for i in range(len(t)):
            dct_t[t[i]] = dct_t.get(t[i], 0) + 1

        min_length = float("inf")
        result = ""
        matches = 0
        dct_s = {}
        left = 0
        for right in range(len(s)):
            dct_s[s[right]] = dct_s.get(s[right], 0) + 1

            if s[right] in dct_t and dct_s[s[right]] == dct_t[s[right]]:
                matches += 1

            while matches == len(dct_t):
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    # result = (left, right)
                    result = s[left:right + 1]

                dct_s[s[left]] -= 1
                if s[left] in dct_t and dct_s[s[left]] < dct_t[s[left]]:
                    matches -= 1
                left += 1

        return result
