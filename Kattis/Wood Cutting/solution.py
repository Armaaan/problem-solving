def minimize_average_waiting_time(test_cases):
    results = []
    for test_case in test_cases:
        all_pieces = []
        for customer in test_case:
            all_pieces.append(sum(customer))
        
        all_pieces.sort()

        total_waiting_time = 0
        current_time = 0
        for piece in all_pieces:
            current_time += piece
            total_waiting_time += current_time

        average_waiting_time = total_waiting_time / len(all_pieces)
        results.append(f"{average_waiting_time:.6f}")

    return results


T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    test_case = []
    for _ in range(N):
        data = list(map(int, input().split()))
        W = data[0]
        sizes = data[1:]
        test_case.append(sizes)
    test_cases.append(test_case)

results = minimize_average_waiting_time(test_cases)
print("\n".join(results))
