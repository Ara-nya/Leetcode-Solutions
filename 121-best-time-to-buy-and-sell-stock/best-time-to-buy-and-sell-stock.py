class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for items in prices:
            cost = items - mini
            profit = max(profit, cost)
            mini = min(mini, items)
        
        return profit