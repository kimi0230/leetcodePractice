# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# int minprice = Integer.MAX_VALUE
# int maxprofit = 0
# for (int i=0, i < prices.length, i++) {
#     if (prices[i] < minprice)
#     minprice = prices[i]
#     else if (prices[i] - minprice > maxprofit)
#     maxprofit = prices[i] - minprice
# }
# return maxprofit


# 從頭找最小  從尾找最大

import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        max_price = 0
        min_price = sys.maxsize

        for val in prices:
            # print(list(reversed(prices)))
            min_price = min(min_price, val)
            profit = val - min_price
            max_price = max(max_price, profit)
        
        return max_price
        

if __name__ == '__main__':
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
