import heapq

Q = int(input())
s = {}
mx, mn = [], []
heapq.heapify(mx)
heapq.heapify(mn)
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        if query[1] not in s:
            s[query[1]] = 1
            heapq.heappush(mx, -query[1])
            heapq.heappush(mn, query[1])
        else: s[query[1]] += 1

    elif query[0] == 2:
        if query[1] not in s: continue
        s[query[1]] -= min(query[2], s[query[1]])
        if not s[query[1]]:
            s.pop(query[1])
            if not s: continue
            if -mx[0] == query[1]: mx.remove(-query[1])
            if mn[0] == query[1]: mn.remove(query[1])

    else: ans.append(-sum(x[0] for x in (mx, mn)))

print(*ans, sep='\n')
