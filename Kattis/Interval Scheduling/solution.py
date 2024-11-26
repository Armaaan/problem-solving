def interval_scheduling():
    n = int(input())
    intervals = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
    selected_intervals = []

    for s, f in intervals:
        if not selected_intervals or s >= selected_intervals[-1][1]:
            selected_intervals.append((s, f))
    
    print(len(selected_intervals))

interval_scheduling()