class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers) - 1
        while first < last:
            if numbers[first] + numbers[last] > target:
                last -= 1
            elif numbers[first] + numbers[last] < target:
                first += 1
            
            if numbers[first] + numbers[last] == target:
                return [first + 1, last + 1]