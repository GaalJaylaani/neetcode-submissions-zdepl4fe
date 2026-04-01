class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        for i in nums:
            if num in nums:
                num += 1
        return num