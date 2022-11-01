#https://www.youtube.com/watch?v=RzT6YgrGTyg
class MyQueue:

    def __init__(self):
        #as a 'stack' to keep track of pushes
        self.s1 = []
        
        #as a 'queue' to help with peeking and popping (front of queue)
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        #s2 empty
        if not self.s2:
            while self.s1:
                #s1 = 3,2,1
                self.s2.append(self.s1.pop())
                #s2 = 1,2,3
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()