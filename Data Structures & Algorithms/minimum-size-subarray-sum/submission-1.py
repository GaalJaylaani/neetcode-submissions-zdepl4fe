class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , total = 0,0
        minS = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                minS = min(minS, r - l + 1)
                total -= nums[l]
                l += 1
        return minS if minS != float('inf') else 0