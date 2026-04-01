class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        minVal = float('inf')

        for r in range(len(prices)):
            minVal = min(minVal, prices[r])
            maxP = max(maxP, prices[r] - minVal)
        return maxP