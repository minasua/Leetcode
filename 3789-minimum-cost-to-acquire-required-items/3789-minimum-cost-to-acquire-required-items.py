class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        x, y, z = cost1, cost2, costBoth
        pairs = min(need1, need2)
        cost = 0
        if z <= x + y: #use both for all pairs
            cost += pairs * z 
        else: 
            cost += pairs * x + pairs * y
        #now left the remaining, compare to z
        delta = abs(need1 - need2)
        if need1 > need2: 
            cost += min(z, x) * delta
        elif need2 > need1:
            cost += min(z, y) * delta
        return cost
