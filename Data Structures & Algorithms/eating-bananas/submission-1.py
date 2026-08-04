class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bs(l, r, piles, hours):
            mid = (l + r) // 2
            time = 0
            if l > r:
                return l

            for x in piles:
                time += math.ceil(x / mid)
            if time <= hours:
                return bs(l, mid-1, piles, hours)
            else:
                return bs(mid+1, r, piles, hours)
        return bs(1, max(piles), piles, h)
