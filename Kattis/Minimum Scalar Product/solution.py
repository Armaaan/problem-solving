T = int(input())
results = []

for t in range(1, T + 1):
    n = int(input())
    fst_line = sorted(map(int, input().split()))
    snd_line = sorted(map(int, input().split()), reverse=True)
    
    total = sum(x * y for x, y in zip(fst_line, snd_line))
    results.append(f"Case #{t}: {total}")

print("\n".join(results))