class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairing = {']': '[',
                   ')': '(',
                   '}': '{'}

        for char in s:
            if char == ' ':
                continue
            if char in pairing.keys() and stk:
                recent = stk.pop()
                print(recent)
                if pairing[char] != recent:
                    return False
            else:
                stk.append(char)
        return len(stk) == 0
        