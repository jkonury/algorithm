class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0

        max_val = 0
        sell = prices[0]
        for i in range(1, size):
            if prices[i] < sell:
                sell = prices[i]
            else:
                max_val = max(max_val, prices[i] - sell)
        return max_val
