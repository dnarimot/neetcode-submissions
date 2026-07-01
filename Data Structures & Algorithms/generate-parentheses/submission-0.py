class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parantheses if open < n
        #only add a closing parantheses if closed < open
        #valid iff open == closed == n
        
        stack = []
        out = []
        openCount = 0
        closeCount = 0

        def backtrack(openCount, closeCount):
            if openCount == closeCount == n:
                #if count is reached, take all elements in stack
                #join them together, append to output array 
                out.append("".join(stack))
                return

            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop() 
                #once backtracking finished, pop the element you added to clear up memory
            
            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()
        
        backtrack(0, 0) #intial run, open and closed counts is 0
        return out

            