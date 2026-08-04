class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        present = [False] * (len(nums) + 1)
        for i in nums:
            if i > 0 and i <= len(nums):
                present[i] = True
        print(present)
        for i in range(1, len(present)):
            if not present[i]:
                return i
                
        return len(nums) + 1