class TimeMap:

    def __init__(self):
        self.dct = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dct.keys():
            self.dct[key] = []
        self.dct[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct.keys():
            return ""

        left = 0
        right = len(self.dct[key]) - 1

        search_list = self.dct[key]
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if search_list[mid][1] <= timestamp:
                result = search_list[mid][0]
                left = mid + 1
            else:
                right = mid - 1
                
        return result




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)