class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(list(zip(position, speed)), reverse = True)
        
        fleets = 0
        max_time = 0
        for pos, speed in sorted_pairs:
            time = (target - pos) / speed
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets