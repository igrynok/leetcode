class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token.isnumeric():
                stack.append(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                num = eval(num1 + token + num2)
                stack.append(str(int(num)))

        return int(stack[0])