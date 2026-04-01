class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = set()
        for n in nums:
            if n in countMap:
                return True
            countMap.add(n)
        return False
         