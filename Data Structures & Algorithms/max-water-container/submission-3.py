class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxwater = 0

        while l < r:
            water = min(heights[l], heights[r]) * (r-l)
            maxwater = max(water, maxwater)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxwater