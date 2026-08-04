class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        premult = []
        mult = 1
        for i in range(len(nums)):
            premult.append(mult)
            mult *= nums[i]
        mult = 1
        for i in range(len(nums) - 1, -1, -1):
            premult[i] *= mult
            mult *= nums[i]
        return premult 