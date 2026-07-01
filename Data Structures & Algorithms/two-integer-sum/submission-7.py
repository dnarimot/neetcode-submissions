class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}
        numsLen = len(nums)
        for i in range(numsLen):
            #store indicies as values and key as num 
            numIndex[nums[i]] = i
        for i in range(numsLen):
            diff = target - nums[i]
            if diff in numIndex.keys() and i != numIndex[diff]:
                return [i, numIndex[diff]]



        
        
        