class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        left = 0
        right = 0 

        while right < len(nums):
            while dq and nums[right] > dq[-1]:
                dq.pop()
            dq.append(nums[right])

            if (right - left + 1) == k:
                result.append(dq[0])
                if nums[left] == dq[0]:
                    dq.popleft()
                left += 1

            right += 1
        
        return result