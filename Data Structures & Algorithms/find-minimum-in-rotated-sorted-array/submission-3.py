class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        left= 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2 
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[left]:
                return nums[left]
            else:
                right = mid - 1
        