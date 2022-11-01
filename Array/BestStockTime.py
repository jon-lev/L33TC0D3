#O(N) runtime
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Set min price to arbitrary first element
        minPrice = prices[0]
        maxProfit = 0
        #Loop through all elements in p
        for p in prices:
            #min price avaliable will be min of old minPrice and current price
            minPrice = min(minPrice, p)
            
            #maxProfit is maximum of difference between price and minPrice or old maxProfit
            maxProfit = max(maxProfit, p - minPrice)
        return maxProfit