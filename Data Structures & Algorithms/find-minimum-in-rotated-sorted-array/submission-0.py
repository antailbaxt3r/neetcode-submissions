class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        answer = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(answer, nums[l])
            mid = (l+r) // 2
            answer = min(answer, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return answer