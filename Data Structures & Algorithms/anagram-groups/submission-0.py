from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = {}
        finalList = []
        for s in strs:
            sortStr = ''.join(sorted(s))
            print(sortStr)
            if sortStr not in sortedStrs:
                sortedStrs[sortStr] = [s]
            else:
                sortedStrs[sortStr].append(s)
        for sublist in sortedStrs.values():
            finalList.append(sublist)
        return finalList

            


        