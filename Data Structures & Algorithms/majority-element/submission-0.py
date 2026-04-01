class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for num, freq in count.items():
            if freq > (len(nums)) // 2:
                return num