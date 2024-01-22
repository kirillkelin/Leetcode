class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_unique = set(nums)
        length_max = 0
        for num in nums_unique:
            if (num + 1) not in nums_unique:
                length = 1
                while (num - length) in nums_unique:
                    length += 1

                length_max = max(length_max, length)

        return length_max