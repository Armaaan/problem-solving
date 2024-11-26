from collections import defaultdict, deque

def shortest_construction_time(n, a, dependencies):
    graph = defaultdict(list)
    indegree = [0] * n
    for i, deps in enumerate(dependencies):
        for dep in deps:
            graph[dep - 1].append(i)
            indegree[i] += 1

    topo_order = []
    queue = deque([i for i in range(n) if indegree[i] == 0])
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    def compute_dp(times):
        dp = [0] * n
        for node in topo_order:
            dp[node] = times[node]
            for dep in dependencies[node]:
                dp[node] = max(dp[node], dp[dep - 1] + times[node])
        return dp

    original_dp = compute_dp(a)
    min_time = original_dp[-1]

    for i in range(n):
        modified_times = a[:]
        modified_times[i] = 0
        new_dp = compute_dp(modified_times)
        min_time = min(min_time, new_dp[-1])

    return min_time

n = int(input())
a = list(map(int, input().split()))
dependencies = []
for _ in range(n):
    deps = list(map(int, input().split()))
    dependencies.append(deps[1:])

print(shortest_construction_time(n, a, dependencies))
