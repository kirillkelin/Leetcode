class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums

        left = 0
        result = []
        for i in range(len(nums)):
            if i != len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                continue
            else:
                if nums[i] == nums[left]:
                    result.append(f"{nums[i]}")
                else:
                    result.append(f"{nums[left]}->{nums[i]}")
                
                left = i + 1
        return result