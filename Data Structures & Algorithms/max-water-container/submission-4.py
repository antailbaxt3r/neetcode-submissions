class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        maxwater = 0

        while l < r:
            water = min(heights[l], heights[r]) * (r-l)
            maxwater = max(water, maxwater)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxwater