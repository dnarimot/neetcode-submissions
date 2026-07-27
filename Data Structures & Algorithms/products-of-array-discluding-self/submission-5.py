class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]
        output = []
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        left_product = 1
        for i in range(len(nums)):
            prefix[i] = left_product
            left_product *= nums[i]
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = right_product
            right_product *= nums[i]
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        return output
        # for i in range(len(nums)):
        #     left_product = 1
        #     for left_i in range(i):
        #         left_product *= nums[left_i]
        #     right_product = 1
        #     for right_i in range(i+1, len(nums)):
        #         right_product *= nums[right_i]
        #     output.append(left_product * right_product)
        # return output

