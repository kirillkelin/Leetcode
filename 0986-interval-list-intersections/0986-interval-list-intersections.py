class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        first = 0 
        second = 0
        result = []

        while first < len(firstList) and second < len(secondList):
            max_val_left = max(firstList[first][0], secondList[second][0])
            min_val_right = min(firstList[first][1], secondList[second][1])

            if max_val_left <= min_val_right:
                result.append([max_val_left, min_val_right])

            if firstList[first][1] > secondList[second][1]:
                second += 1
            else:
                first += 1

        return result