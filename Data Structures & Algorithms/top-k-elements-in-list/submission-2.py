class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        reverse_counts = [[] for _ in range(len(nums) + 1)]
        for key, v in count.items():
            reverse_counts[v].append(key)
        answer = []
        for i in range(len(reverse_counts) - 1, 0, -1):
            for n in reverse_counts[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer

        