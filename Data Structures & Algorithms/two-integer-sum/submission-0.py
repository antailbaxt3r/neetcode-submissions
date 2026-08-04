class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        k = target
        for i, val in enumerate(nums):
            if k - val in hashmap:
                return [hashmap[k-val], i]
            else:
                hashmap[val] = i
        return None
