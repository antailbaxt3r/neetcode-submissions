class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l, r, nums, target):
            mid = (l + r) // 2
            if l == r:
                return -1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bs(l, mid, nums, target)
            else:
                return bs(mid+1, r, nums, target)
        return bs(0, len(nums), nums, target)
