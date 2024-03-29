import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
G = [set() for _ in range(N)]
cost = [0]*N
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)
    cost[u] += A[v]
    cost[v] += A[u]

hq = [[cost[i], i] for i in range(N)]
heapq.heapify(hq)

ans = 0
erased = [False]*N
while hq:
    print(cost)
    c, u = heapq.heappop(hq)
    if erased[u]: continue
    erased[u] = True
    ans = max(ans, c)

    for v in G[u]:
        if erased[v]: continue
        cost[v] -= A[u]
        heapq.heappush(hq, [cost[v], v])

print(ans)
