from collections import Counter
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        #A question to ask in interview is: do the lengths of the string need to match?
        #two methods: iterate through both, creating set of letters in both, then comparing two sets
        #Or, iterate through one, creating set and then itrating other and soon as letter not in set, return false
        if len(s) != len(t):
            return False
        hashMapS = Counter(s)
        hashMapT = Counter(t)
        return hashMapS == hashMapT
