class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}

        for word in strs:
            tup = tuple(sorted(word))
            if tup in sublists:
                sublists[tup].append(word)
            else:
                sublists[tup] = [word]
        
        output = []
        for sublist in sublists.values():
            output.append(sublist)

        return output