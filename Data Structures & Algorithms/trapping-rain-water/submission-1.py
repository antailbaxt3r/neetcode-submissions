class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        for i in range(len(height)):
            lmax = rmax = height[i]
            for j in range(i):
                lmax = max(lmax, height[j])
            for j in range(i+1, len(height)):
                rmax = max(rmax, height[j])
            answer += min(lmax, rmax) - height[i]
        return answer
