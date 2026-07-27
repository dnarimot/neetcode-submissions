class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            left_product = 1
            for left_i in range(i):
                left_product *= nums[left_i]
            right_product = 1
            for right_i in range(i+1, len(nums)):
                right_product *= nums[right_i]
            output.append(left_product * right_product)
        return output
