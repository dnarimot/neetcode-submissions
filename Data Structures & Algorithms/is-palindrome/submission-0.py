class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            isLeft = s[left].isalnum()
            isRight = s[right].isalnum()
            if isLeft and isRight:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            if not isLeft:
                left += 1
            if not isRight:
                right -= 1
        return True
            

            
                