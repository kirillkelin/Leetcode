class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:    
        if len(s1) > len(s2):
            return False

        dct_1 = {key: 0 for key in range(26)}
        dct_2 = {key: 0 for key in range(26)}

        for i in range(len(s1)):
            dct_1[ord(s1[i]) - ord("a")] += 1
            dct_2[ord(s2[i]) - ord("a")] += 1

        left = 0
        
        for i in range(len(s1), len(s2) + 1):
            if dct_1 == dct_2:
                return True
            else:
                if i == len(s2):
                    break

            dct_2[ord(s2[left]) - ord("a")] -= 1
            left += 1
            dct_2[ord(s2[i]) - ord("a")] += 1

        
        return False