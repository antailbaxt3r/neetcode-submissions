class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            if target - val in hashmap:
                return [hashmap[target-val], i]
            else:
                hashmap[val] = i