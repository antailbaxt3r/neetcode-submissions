class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        res = []
        freq = [[] for _ in range(len(nums)+1)]
        for key, v in count.items():
            freq[v].append(key)
        for i in range(len(freq)-1, -1, -1):
            for x in freq[i]:
                res.append(x)
                if len(res) == k:
                    return res
        return res