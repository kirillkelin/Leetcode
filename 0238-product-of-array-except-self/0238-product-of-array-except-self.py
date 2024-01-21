class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_left = []
        value_left = 1
        value_right = 1
        for i in range(len(nums)):
            if i == 0:
                result_left.append(value_left)
            else:
                value_left *= nums[i-1]
                result_left.append(value_left) 
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            else:
                value_right *= nums[i+1]
                result_left[i] *= value_right
        return result_left
        
