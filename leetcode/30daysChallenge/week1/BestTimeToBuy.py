# Say you have an array prices for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again)

class Solution:

# 200 / 200 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 15.1 MB
	def maxProfit(self, prices):
		n = len(prices)
		profit = 0
		for i in range(1, n):
			if prices[i-1] < prices[i]:
				profit += prices[i] - prices[i-1]
		return profit

class Solution_2:
# 	Runtime: 60 ms
# Memory Usage: 15.1 MB
    def maxProfit(self, prices):
        profit = 0
        stock = 0 # holds the value of stock we purchased
        bought = False
        
        for i in range(len(prices)):
            currDayValue = prices[i]
            nextDayValue = prices[i+1] if i != len(prices) -1 else -1   # Handle Edge Case
            print(i, currDayValue, nextDayValue)
            
            if not bought and currDayValue < nextDayValue:
                stock = currDayValue
                bought = True
                print("bought", stock)
            elif bought and stock < currDayValue and currDayValue > nextDayValue:
                profit += currDayValue - stock
                stock = 0  # we sold the stock
                bought = False
                print("sell", currDayValue)
                print("profit", profit)
        
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: # edge case
            return 0
        
        # take down positive daily return only
        profit = [] 
        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1])) 
        return sum(profit)

			


if __name__ =="__main__":
	prices = [7,1,2,3,1, 100]
	print(Solution_2().maxProfit(prices))