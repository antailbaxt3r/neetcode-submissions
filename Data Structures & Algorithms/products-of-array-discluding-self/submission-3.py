class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = []
        postprod = [1 for _ in nums]

        prefix = 1
        for num in nums:
            preprod.append(prefix)
            prefix *= num
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            postprod[i] = (prefix)
            prefix *= nums[i]
        ans = []
        for i, j in zip(preprod, postprod):
            ans.append(i * j)

        return ans