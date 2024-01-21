class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dct = {}
        
        for letter in s:
            if letter not in dct.keys():
                dct[letter] = 1
            else:
                dct[letter] += 1

        for char in t:
            if char not in dct.keys():
                return False
            dct[char] -= 1

        for value in dct.values():
            if value != 0:
                return False
        return True 