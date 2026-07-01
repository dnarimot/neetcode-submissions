class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}
        numsLen = len(nums)
        for i in range(numsLen):
            #store indicies as values and key as num 
            if nums[i] not in numIndex.keys():
                numIndex[nums[i]] = [i]
            else:
                return numIndex[nums[i]] + [i]
        for i in range(numsLen):
            diff = target - nums[i]
            if diff in numIndex.keys() and i not in numIndex[diff]:
                return [i] + numIndex[diff]



        
        
        