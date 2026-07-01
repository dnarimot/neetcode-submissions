class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        sublists = {}
        for i in range(len(strs)):
            temp = {}
            for char in strs[i]:
                if char in temp:
                    temp[char] += 1
                else:
                    temp[char] = 1
            tuple_temp = tuple(sorted(temp.items()))
            if tuple_temp in sublists.keys():
                sublists[tuple_temp].append(strs[i])
            else:
                sublists[tuple_temp] = [strs[i]]
        return list(sublists.values())
