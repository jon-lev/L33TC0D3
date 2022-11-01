#Runtime: O(N)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #Holding values throughout calculations
        totalGas = 0
        totalCost = 0
        currTank = 0
        start = 0
        for i in range(len(gas)):
            totalCost = totalCost + cost[i]
            totalGas = totalGas + gas[i]
            
            #Current tank is equal to the gas able to be taken at one station - cost to next
            currTank = currTank + gas[i] - cost[i]
            
            #If you run out of gas, check another start
            if(currTank < 0):
                start = i+1
                currTank = 0
        
        #If the gas offered is less than the cost of gas then no solution
        if(totalGas < totalCost):
            return -1
        else:
            return start
                