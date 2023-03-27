# time: O(N)
# space: O(N)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            # 紀錄到當前步數的最低價格
            cost[i] += min(cost[i-2], cost[i-1])

        # 回傳最低總價格
        return min(cost[-2], cost[-1])