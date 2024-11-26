def max_mink_slaughtered(n, k, mink_counts):
    dp = [0] * (k + 1)
    for m in mink_counts:
        for j in range(k, m - 1, -1):
            dp[j] = max(dp[j], dp[j - m] + m)
    return dp[k]

n, k = map(int, input().split())
mink_counts = [int(input()) for _ in range(n)]
print(max_mink_slaughtered(n, k, mink_counts))
