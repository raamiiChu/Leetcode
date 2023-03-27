# time: O(N)
# space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = float(inf)  # 最小購買價格
        max_profit = 0  # 最大利潤

        # 計算當前利潤和更新最大利潤
        for price in prices:
            min_buy_price = min(min_buy_price, price)
            max_profit = max(max_profit, price - min_buy_price)
        
        return max_profit