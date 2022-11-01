class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for s in tokens:
            if s in "+*/-":
                num1 = stack.pop()
                num2 = stack.pop()
                num1 = int(num1)
                num2 = int(num2)
                
                if s == "+":
                    stack.append(num1 + num2)
                elif s == '-':
                    #have to make sure order of numbers is correct 
                    stack.append(num2 - num1)
                elif s == '*':
                    stack.append(num1 * num2)
                elif s == '/':
                    #need to do this for division, // doesn't work for a +num/-num
                    stack.append(int(float(num2) / num1))
            else:
                stack.append(s)
        
        return stack.pop()
                