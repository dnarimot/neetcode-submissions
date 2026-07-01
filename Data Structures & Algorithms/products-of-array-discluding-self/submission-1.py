class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        while i < len(nums):
            left = 1
            right = 1
            for num in nums[:i]:
                left *= num
            for num in nums[i+1:]:
                right *= num
            output.append(left * right)
            i += 1
        return output