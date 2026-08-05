class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(nums, l, r, target):
            if r-l <= 0:
                if nums[l] == target:
                    return l
                else:
                    return -1
                    
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return bs(nums, m+1, r, target)
            else:
                return bs(nums, l, m-1, target)
        return bs(nums, 0, len(nums)-1, target)
            
