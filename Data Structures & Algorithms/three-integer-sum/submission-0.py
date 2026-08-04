class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = set()

        for i in range(n-1):
            j = i + 1
            k = n - 1

            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    answer.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    k -= 1
        return list(answer)