from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = float('inf')
        p1, p2, p3 = 0, INF, INF   # best cost to reach j-1, j-2, j-3
        for j in range(1, n + 1):
            cur = costs[j - 1] + min(p1 + 1, p2 + 4, p3 + 9)
            p3, p2, p1 = p2, p1, cur
        return p1