class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    stack.append(int(first / second))
        return stack.pop()