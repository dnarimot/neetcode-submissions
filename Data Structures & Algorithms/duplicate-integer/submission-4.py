class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            temp = seen.get(num, 0)
            if temp == 1:
                return True
            else:
                seen[num] = 1
        return False

