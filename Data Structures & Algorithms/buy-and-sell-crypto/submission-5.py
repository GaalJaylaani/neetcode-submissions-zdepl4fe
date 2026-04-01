class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minVal = float('inf')
        for r in range(len(prices)):
            minVal = min(prices[r], minVal)
            maxP = max(maxP, prices[r] - minVal)
        return maxP