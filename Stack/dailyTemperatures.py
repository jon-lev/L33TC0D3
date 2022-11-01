class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            #while the stack has values and the top of stack is less than curr temperature (found a future temp that is greater than previous ones, set time to index - curr)
            while stack and temperatures[stack[-1]] < t:
                curr = stack.pop()
                ans[curr] = i - curr
            stack.append(i)
        
        return ans