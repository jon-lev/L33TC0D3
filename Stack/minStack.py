class MinStack:

    def __init__(self):
        self.s1 = []

    def push(self, val: int) -> None:
        currMin = self.getMin()
        if currMin == None or val < currMin:
            currMin = val
        self.s1.append((val, currMin))

    def pop(self) -> None:
        self.s1.pop()

    def top(self) -> int:
        #top of the stack will be the last value (b/c appending to end during push)
        if self.s1:
            return self.s1[-1][0]

    def getMin(self) -> int:
        #Store currMin as second value in tuple (easily found as last element of list)
        if self.s1:
            return self.s1[-1][1]
        return float("inf")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()