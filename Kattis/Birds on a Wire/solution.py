def additional_birds(l, d, n, positions):
    if n == 0:
        return (l - 12) // d + 1

    additional = 0
    positions.sort()

    start = 6
    distance = positions[0] - d
    if distance >= start:
        additional += (distance - start) // d + 1

    if n > 1:
        for i in range(1, n):
            gap_start = positions[i - 1] + d
            gap_end = positions[i] - d
            if gap_end > gap_start:
                additional += (gap_end - gap_start) // d + 1

    last_bird_end = positions[-1] + d
    end = l - 6
    if end >= last_bird_end:
        additional += (end - last_bird_end) // d + 1

    return additional

l, d, n = map(int, input().split())
positions = [int(input()) for _ in range(n)]

print(additional_birds(l, d, n, positions))