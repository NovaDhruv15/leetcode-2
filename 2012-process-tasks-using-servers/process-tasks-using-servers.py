import heapq
from typing import List
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        res = []
        t = 0
        for j, d in enumerate(tasks):
            t = max(t, j)
            if not free:
                t = max(t, busy[0][0])
            while busy and busy[0][0] <= t:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            res.append(i)
            heapq.heappush(busy, (t + d, w, i))
        return res