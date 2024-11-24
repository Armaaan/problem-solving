def maximum_discount(n, prices):
    prices.sort(reverse=True)
    return sum(prices[i] for i in range(2, n, 3))

n = int(input())
prices = list(map(int, input().split()))
print(maximum_discount(n, prices))
