from pathlib import Path
import pandas as pd


def divide_and_conquer(p, lo, hi):
    if lo == hi:
        return 0, lo, lo
    mid = (lo + hi) // 2
    left = divide_and_conquer(p, lo, mid)
    right = divide_and_conquer(p, mid + 1, hi)
    buy = min(range(lo, mid + 1), key=lambda i: p[i])
    sell = max(range(mid + 1, hi + 1), key=lambda i: p[i])
    return max(left, right, (p[sell] - p[buy], buy, sell))


def linear_scan(p):
    low = 0
    best = (0, 0, 0)
    for i in range(len(p)):
        if p[i] < p[low]:
            low = i
        best = max(best, (p[i] - p[low], low, i))
    return best


prices = pd.read_csv(Path(__file__).parent / "prices.csv")["price"].tolist()
print("Number of days:", len(prices))

profit, buy, sell = divide_and_conquer(prices, 0, len(prices) - 1)
print("Divide and conquer: buy on day", buy, "sell on day", sell, "profit", profit)

profit, buy, sell = linear_scan(prices)
print("Linear scan: buy on day", buy, "sell on day", sell, "profit", profit)