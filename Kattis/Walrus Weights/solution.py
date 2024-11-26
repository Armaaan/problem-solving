n = int(input())
weights = [int(input()) for _ in range(n)]
target = 1000
dp = [False] * (target + max(weights) + 1)
dp[0] = True

for weight in weights:
    for j in range(len(dp) - 1, weight - 1, -1):
        dp[j] = dp[j] or dp[j - weight]

closest_sum = 0
for i in range(len(dp)):
    if dp[i]:
        if abs(i - target) < abs(closest_sum - target) or (abs(i - target) == abs(closest_sum - target) and i > closest_sum):
            closest_sum = i

print(closest_sum)
