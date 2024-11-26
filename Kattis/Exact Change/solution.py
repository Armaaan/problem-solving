def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    index = 1

    for _ in range(t):
        price = int(data[index])
        index += 1
        n = int(data[index])
        index += 1
        coins = list(map(int, data[index:index + n]))
        index += n
        
        coins.sort()
        dp = [(float('inf'), float('inf'))] * (10001)
        dp[0] = (0, 0)
        
        for coin in coins:
            for i in range(10000, coin - 1, -1):
                if dp[i - coin][0] + coin < dp[i][0] or (dp[i - coin][0] + coin == dp[i][0] and dp[i - coin][1] + 1 < dp[i][1]):
                    dp[i] = (dp[i - coin][0] + coin, dp[i - coin][1] + 1)
        
        for i in range(price, 10001):
            if dp[i][0] != float('inf'):
                results.append(f"{dp[i][0]} {dp[i][1]}")
                break
    
    print("\n".join(results))


solve()
