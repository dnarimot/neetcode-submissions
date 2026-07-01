class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        out =[]
        length = len(nums)
        while i < length:
            right, left = 1, 1
            for num in nums[:i]:
                left *= num
            if i != length - 1:
                for num in nums[i+1:]:
                    right *= num
            out.append(left*right)
            i += 1
        return out