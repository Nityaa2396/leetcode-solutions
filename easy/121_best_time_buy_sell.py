# Problem 121: Best Time to Buy and Sell Stock
# Find max profit from one buy and one sell
# Input: [7,1,5,3,6,4] → 5 | [7,6,4,3,1] → 0

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print(max_profit([7,1,5,3,6,4]))  # 5
print(max_profit([7,6,4,3,1]))    # 0