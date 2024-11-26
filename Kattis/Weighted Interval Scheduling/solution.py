def weighted_interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    dp = [0] * (n + 1)
    p = [0] * n

    def binary_search(intervals, i):
        start_time = intervals[i][0]
        low, high = 0, i - 1
        while low <= high:
            mid = (low + high) // 2
            if intervals[mid][1] <= start_time:
                if intervals[mid + 1][1] <= start_time:
                    low = mid + 1
                else:
                    return mid + 1
            else:
                high = mid - 1
        return 0

    for i in range(n):
        p[i] = binary_search(intervals, i)

    for i in range(1, n + 1):
        s, f, w = intervals[i - 1]
        dp[i] = max(dp[i - 1], dp[p[i - 1]] + w)

    return dp[n]

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
print(weighted_interval_scheduling(intervals))
