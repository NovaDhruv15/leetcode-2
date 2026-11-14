class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n, best = len(nums), float('inf')
        for i in range(n):
            s = 0
            for j in range(i, min(n, i + r)):
                s += nums[j]
                if j - i + 1 >= l and s > 0:
                    best = min(best, s)
        return best if best != float('inf') else -1