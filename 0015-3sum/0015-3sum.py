class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 1):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            first = i + 1
            last = len(nums) - 1

            while first < last:
                search_sum = nums[first] + nums[last]
                if search_sum > target:
                    last -= 1
                elif search_sum < target:
                    first += 1
                else: 
                    result.append([nums[i], nums[first], nums[last]])
                    first += 1
                    while nums[first] == nums[first - 1] and first < last:
                        first += 1

        return result

        # nums = sorted(nums)
        # dct = {}
        # result = []
        # for i in range(len(nums)):
        #     target = 0 - nums[i]
        #     for key in dct.keys():
        #         dct[key] -= 1
        #         search_num = target - key                
        #         if (search_num in dct) and (dct[search_num] != 0):
        #             if sorted([nums[i], key, search_num]) in result:
        #                 dct[key] += 1
        #                 continue
        #             else: 
        #                 result.append(sorted([nums[i], key, search_num]))
        #         dct[key] += 1
        #     dct[nums[i]] = dct.get(nums[i], 0) + 1
        
        # return result


