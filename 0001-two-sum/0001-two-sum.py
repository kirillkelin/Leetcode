class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            emp = target - nums[i]
            if emp in dct:
                return(dct[emp], i)
            dct[nums[i]] = i