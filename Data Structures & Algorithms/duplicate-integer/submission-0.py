class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allNums = set()

        for val in nums: #for every value in array
            if val in allNums: #if value in set aka duplicate, return true
                return True
            else:
                allNums.add(val)
        return False #return if no duplicate appeared in set 

