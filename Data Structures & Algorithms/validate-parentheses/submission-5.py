class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        pair = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        for char in s:
            if char == "}" or char == ")" or char == "]": 
                if len(stack) == 0:
                    return False
                elif stack.pop() != pair[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0