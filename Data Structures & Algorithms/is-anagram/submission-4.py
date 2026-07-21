class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #using ASCII to grab letter's index and update counts in a list
        #
        if len(s) != len(t):
            return False
        countS = [0] * 26
        countT = [0] * 26
        for i in range(len(s)):
            countS[122 - ord(s[i])] += 1
            countT[122 - ord(t[i])] += 1
        
        return countS == countT
