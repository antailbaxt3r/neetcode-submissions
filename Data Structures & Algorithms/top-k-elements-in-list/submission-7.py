class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        for key, val in counts.items():
            freq[val].append(key)
        answer = []
        for i in range(len(freq)-1, -1, -1):
            answer = answer + freq[i]
            if len(answer) == k:
                return answer
        return []
        
             