from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sort = count.most_common(k)
        out = []
        for tup in sort:
            out.append(tup[0])
        return out