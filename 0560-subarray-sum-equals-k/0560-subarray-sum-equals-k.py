class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0: 1}
        result = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in dct:
                result += dct[prefix_sum - k]
            
            dct[prefix_sum] = dct.get(prefix_sum, 0) + 1

        return result

