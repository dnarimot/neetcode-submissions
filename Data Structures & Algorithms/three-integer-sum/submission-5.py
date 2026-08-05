class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        new_nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            if new_nums[i] > 0:
                break
            if i > 0 and new_nums[i] == new_nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sumNums = new_nums[j] + new_nums[k]
                if sumNums == -new_nums[i]:
                    output.append([new_nums[i], new_nums[j], new_nums[k]])
                    j += 1
                    while j < k and new_nums[j] == new_nums[j-1]:
                        j += 1
                elif sumNums < -new_nums[i]:
                    j += 1
                elif sumNums > -new_nums[i]:
                    k -= 1
        return output
                
        