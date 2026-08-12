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
                #cutoff is on right of mid
                left = mid + 1
            #either mid is min or cutoff is to the left
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            else:
                if nums[mid] > nums[left]:
                    return nums[left]
                else:
                    right = mid - 1
        