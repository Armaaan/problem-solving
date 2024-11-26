def max_farms_closed(n, k, mink_counts):
    mink_counts.sort()
    total_mink = 0
    farms_closed = 0
    for m in mink_counts:
        if total_mink + m <= k:
            total_mink += m
            farms_closed += 1
        else:
            break
    return farms_closed

n, k = map(int, input().split())
mink_counts = [int(input()) for _ in range(n)]
print(max_farms_closed(n, k, mink_counts))
