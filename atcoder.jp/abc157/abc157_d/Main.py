def main():
    N, M, K = map(int, input().split())
    ans = [0]*N
    dsu = DSU(N)
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        ans[a] -= 1
        ans[b] -= 1
        dsu.merge(a, b)

    for _ in range(K):
        c, d = map(lambda x: int(x)-1, input().split())
        if dsu.same(c, d):
            ans[c] -= 1
            ans[d] -= 1

    for g in dsu.groups():
        for i in g: ans[i] += len(g)-1

    print(*ans)


class DSU:
    def __init__(self, n):
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.leader(a), self.leader(b)
        if x == y: return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]: x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self._n
        if self.parent_or_size[a] < 0: return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self._n
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [self.leader(i) for i in range(self._n)]
        result = [[] for _ in range(self._n)]
        for i in range(self._n): result[leader_buf[i]].append(i)
        return [r for r in result if r != []]


if __name__ == '__main__': main()
