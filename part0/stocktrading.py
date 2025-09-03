def maxProfit(prices):
    if indexof(max(prices))<indexof(min(prices)):
        return max(prices)-min(prices)
    else:
        days = len(prices)
        maxProfit = 0
        for i in range(days):
            for j in range(i,days):
                profit = prices[j] - prices[i]
                if profit>maxProfit:
                    maxProfit = profit
        return maxProfit

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))