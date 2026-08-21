class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        answer = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(answer, nums[l])
            m = (r+l) // 2
            answer = min(answer, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return answer