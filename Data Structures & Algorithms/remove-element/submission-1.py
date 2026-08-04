class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
            
        pointer = len(nums) - 1
        while nums[pointer] == val and pointer > -1:
            pointer -= 1
            print(pointer, nums[pointer])

        
        
        for i, v in enumerate(nums):
            if v == val:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                print(nums)
            while nums[pointer] == val and pointer > -1:
                pointer -= 1  
                print(pointer, nums[pointer])
            if i >= pointer:
                break
        return pointer+1