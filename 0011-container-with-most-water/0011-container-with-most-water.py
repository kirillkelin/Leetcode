class Solution:
    def maxArea(self, height: List[int]) -> int:
        first, last = 0, len(height) - 1 
        max_square = 0

        while first < last:
            current_square = min(height[first], height[last]) * (last - first)
            if height[first] > height[last]:
                last -= 1
            else:
                first += 1
            max_square = max(current_square, max_square)
        return max_square