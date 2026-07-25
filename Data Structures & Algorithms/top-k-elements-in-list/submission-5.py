class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq.keys():
                freq[num] += 1
            else:
                freq[num] = 1
        output = []
        for key, val in sorted(freq.items(), key=lambda item: item[1], reverse=True):
            output.append(key)
        return output[0:k]


