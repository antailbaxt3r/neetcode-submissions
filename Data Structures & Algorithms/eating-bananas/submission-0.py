class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            mid = (l+r) // 2

            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / mid)
            if total_time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res