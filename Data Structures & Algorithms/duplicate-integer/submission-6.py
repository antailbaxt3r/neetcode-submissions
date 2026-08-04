class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for v in hashmap.values():
            if v >= 2:
                return True
        return False
