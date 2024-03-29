import heapq


def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))


class Multiset():
    def __init__(self):
        self.addset = []
        self.delset = []

    def add(self, value): heapq.heappush(self.addset, value)

    def discard(self, value): heapq.heappush(self.delset, value)

    def smallest(self):
        while self.delset and self.addset[0] == self.delset[0]:
            heapq.heappop(self.addset)
            heapq.heappop(self.delset)
        return self.addset[0]

    def is_empty(self): return len(self.addset) - len(self.delset) <= 0


if __name__ == '__main__': main()
