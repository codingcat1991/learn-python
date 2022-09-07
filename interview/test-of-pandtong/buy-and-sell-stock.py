def max_profit(price_list):
    if len(price_list) <= 1:
        return 0
    min_price = price_list[0]
    profit = 0
    for price in price_list:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


print(max_profit([1, 9, 2, 8]))
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))


