class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = [0 for _ in range(len(nums))]
        posprod = [0 for _ in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            preprod[i] = (prefix)
            prefix *= nums[i]
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            posprod[i] = (prefix)
            prefix *= nums[i]
        answer = []
        for i, j in zip(preprod, posprod):
            answer.append(i * j)
        return answer
