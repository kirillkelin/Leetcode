class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dct.keys():
                dct[sorted_word] = [word]
            else:
                dct[sorted_word].append(word) 

        return [i for i in dct.values()]


