class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l < r:
                val = nums[i] + nums[l] + nums[r]

            
                if val == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif val > 0:
                    r -= 1
                else:
                    l += 1
        return ans
            