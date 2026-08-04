class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        prefix = [[]]
        for i in nums:
            prefix += [subset + [i] for subset in prefix]
        return prefix
