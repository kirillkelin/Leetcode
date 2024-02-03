class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_size = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_size = max(max_size, right - left + 1 - zero_count)

        if max_size == len(nums):
            return max_size - 1
        else: 
            return max_size