class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memory = {}
        for index, i in enumerate(numbers):
            if target - i in memory:
                return [memory[target - i] + 1, index + 1]
            else:
                memory[i] = index
        return []