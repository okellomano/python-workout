"""
You are given an array prices where prices[i] is the price of a given stock in ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example:
Input: prices = [9,1,5,3,7,5]
output: 6

Possible clarifying questions:
    ; Can I sell before I buy?
"""

def maximum_profit(prices):
    """Return the maximum profit. """
    max_profit = 0
    left = 0  # buying
    right  = 1  # selling

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    return max_profit

prices = [9,1,5,3,7,5]
print(f'The maximum price returned is: {maximum_profit(prices)}')

