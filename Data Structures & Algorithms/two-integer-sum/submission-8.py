class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            if target - nums[i] in diff.keys():
                return [diff[target-nums[i]], i]
            else:
                diff[nums[i]] = i
        
        


        
        
        