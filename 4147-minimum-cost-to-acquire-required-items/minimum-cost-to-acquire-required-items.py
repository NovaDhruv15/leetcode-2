class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        smaller = min(need1, need2)
        larger = max(need1, need2)
        cost_a = need1 * cost1 + need2 * cost2
        if need1 >= need2:
            leftover = need1 - smaller
            leftover_cost = min(cost1, costBoth)
        else:
            leftover = need2 - smaller
            leftover_cost = min(cost2, costBoth)
        cost_b = smaller * costBoth + leftover * leftover_cost
        cost_c = larger * costBoth
        return min(cost_a, cost_b, cost_c)