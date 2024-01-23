class Solution:
        def trap(self, height: List[int]) -> int:
            idx_max = 0
            for i in range(1, len(height)):
                if height[i] > height[idx_max]:
                    idx_max = i

            result = 0
            max_height_left = 0
            for i in range(0, idx_max):
                if height[i] > max_height_left:
                    max_height_left = height[i]
                else:
                    result += max_height_left - height[i]

            max_height_right = 0
            for i in range(len(height) - 1, idx_max, -1):
                if height[i] > max_height_right:
                    max_height_right = height[i]
                else:
                    result += max_height_right - height[i]

                    
            return result

