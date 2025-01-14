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

def max_profit(prices):
    """Return the maximum profit. """
    profit = 0
    buying = 0
    selling = buying + 1

    while buying < len(prices):
        sell = prices[selling] - prices[buying]

        if sell > profit:
            profit = sell
        selling += buying
    buying += 1
    return profit

prices = [9,1,5,3,7,5]
print(f'The maximum price returned is: {max_profit(prices)}')
