class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        first, last = 0, len(s) - 1
        while first < last:
            if s[first] == s[last]:
                first += 1
                last -= 1
            else:
                return False
        return True