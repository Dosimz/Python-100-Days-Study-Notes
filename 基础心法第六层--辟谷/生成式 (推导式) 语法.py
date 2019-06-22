prices = {
    'APPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# 用股票价格大于 100 元的股票构造一个新的字典
prices_100 = {key: value for key, value in prices.items() if value > 100}
print(prices_100)