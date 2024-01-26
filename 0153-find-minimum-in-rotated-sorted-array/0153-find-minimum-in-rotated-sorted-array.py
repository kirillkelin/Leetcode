class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            result = min(nums[left], result)
            mid = (right + left) // 2
            result = min(nums[mid], result)
            if nums[left] <= nums[mid]:
                left = mid + 1 
            else:
                right = mid - 1

        return result
        
        
        # if len(nums) == 1:
        #     return nums[0]

        # left = 0
        # right = len(nums) - 1

        # while left < right:
        #     mid = (right + left) // 2
            
        #     if nums[left] > nums[right] and nums[mid] < nums[right]:
        #         right = mid
        #     elif nums[left] > nums[right] and nums[mid] > nums[right]:
        #         left = mid + 1
        #     elif nums[left] < nums[right]:
        #         return nums[left]
             
        # return nums[left]


        
        