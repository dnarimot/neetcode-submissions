class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            temp = tuple(sorted(s))
            if temp in hashMap.keys():
                hashMap[temp].append(s)
            else:
                hashMap[temp] = [s]
        return_list = []
        for val in hashMap.values():
            return_list.append(val)
        return return_list