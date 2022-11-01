class TimeMap:

    def __init__(self):
        self.dic = {} #key = string: list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
            if key not in self.dic:
                self.dic[key] = []
            self.dic[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arr = self.dic.get(key, [])
        n = len(arr)
        
        left = 0
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2
            time = arr[mid][1]
            if time <= timestamp:
                #Potential valid result so update return
                res = arr[mid][0]
                left = mid + 1
            elif time > timestamp:
                right = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)