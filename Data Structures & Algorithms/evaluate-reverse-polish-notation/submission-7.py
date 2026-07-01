class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
                print(stack)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
                print(stack)
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first*second)
                print(stack)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                if abs(first) < abs(second):
                    stack.append(0)
                else:
                    stack.append(int(first/second))
                print(stack)
            else:
                stack.append(int(token))
        return int(stack.pop())
                