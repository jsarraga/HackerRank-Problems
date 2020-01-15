# Complete the maximumToys function below.
def maximumToys(prices, k):
    counter = 0
    prices = sorted(prices)
    for i in prices:
        if i <= k:
            k -= i
            counter += 1
    return counter