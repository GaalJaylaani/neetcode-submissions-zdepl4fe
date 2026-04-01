class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxWater = 0
        while left < right:
            minVal = min(heights[left], heights[right])
            width = right - left
            maxWater = max(maxWater, minVal * width)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater