class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for i, cnt in hashmap.items():
            count[cnt].append(i)
        
        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res