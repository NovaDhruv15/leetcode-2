from functools import cache
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        @cache
        def cost(l, r):
            length = r - l + 1
            best = INF
            for step in range(1, length):
                if length % step:
                    continue
                fixes = 0
                for start in range(step):
                    i = l + start
                    j = i + (length // step - 1) * step
                    while i < j:
                        if s[i] != s[j]:
                            fixes += 1
                        i += step
                        j -= step
                best = min(best, fixes)
            return best
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for parts in range(1, k + 1):
            for end in range(2, n + 1):
                for start in range(end - 1): 
                    if dp[parts - 1][start] < INF:
                        dp[parts][end] = min(
                            dp[parts][end],
                            dp[parts - 1][start] + cost(start, end - 1),
                        )
        return dp[k][n]