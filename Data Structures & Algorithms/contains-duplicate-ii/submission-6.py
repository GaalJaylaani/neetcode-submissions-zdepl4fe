class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = set()

        for r, val in enumerate(nums):
            if val in window:
                return True
            
            window.add(val)

            if (r - l) >= k:
                window.remove(nums[l])
                l += 1
        return False

