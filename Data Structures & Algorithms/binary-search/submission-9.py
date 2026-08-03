class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        while left <= right:
            index = (left + right) // 2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                left = index + 1
            elif nums[index] > target:
                right = index - 1
            
        return -1