class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for key, v in count.items():
            freq[v].append(key)
        
        answer = []
        for i in range(len(freq)-1, -1, -1):
            answer = answer + freq[i]
            if len(answer) == k:
                return answer
        
             