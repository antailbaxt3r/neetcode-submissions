class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] = count[i] + 1
            else:
                count[i] = 1
        rev_count = [[] for _ in range(len(nums) + 1)]
        for (key, v) in count.items():
            rev_count[v].append(key)
        print(rev_count)
        ans = []
        for i in range(len(rev_count)-1, -1, -1):
            if rev_count[i]:
                ans = ans + rev_count[i]
            if len(ans) == k:
                return ans
        return ans

             