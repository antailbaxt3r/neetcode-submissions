class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for i, val in enumerate(nums):
            if val == candidate:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                candidate = nums[i]
        return candidate