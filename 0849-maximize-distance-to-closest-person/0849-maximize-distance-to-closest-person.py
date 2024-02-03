class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = -1
        max_dis = 0

        for right in range(len(seats)):
            if seats[right] == 1:
                if left == -1:
                    max_dis = right
                else:
                    max_dis = max((right - left) // 2, max_dis)

                left = right    

        return max(max_dis, len(seats) - 1 - left)