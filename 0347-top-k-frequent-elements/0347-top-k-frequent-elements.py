class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        l = []
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        
        result = sorted(dct.items(), key=lambda x: x[1], reverse = True)
    
        for i in range (k):
            l.append(result[i][0])
        return l

        # l = [[] for _ in range (len(nums) + 1)]

        # for key, value in dct.items():
        #     l[value].append(key)

        # result = []

        # for i in range(len(l) - 1, 0, -1):
        #     for num in l[i]:
        #         result.append(num)
        #         if len(result) == k:
        #             return result

        
         