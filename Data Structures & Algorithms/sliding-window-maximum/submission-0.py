class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        res = []
        dq = deque()

        for r in range(len(nums)):

            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()

            dq.append(r)

            if dq[0] <= r - k:
                dq.popleft()

            if r + 1 >= k:
                res.append(nums[dq[0]])
        return res

            
