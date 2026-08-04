class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        total = 0

        lmax, rmax = 0, 0

        while l <= r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)

            lh, rh = lmax - height[l], rmax - height[r]

            if height[l] < height[r]:
                total += lh
                l += 1
            else:
                total += rh
                r -= 1
        return total