class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operations = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    num = num2 + num1
                elif token == '-':
                    num = num2 - num1
                elif token == '*':
                    num = num2*num1
                elif token == '/':
                    num = int(num2/num1)
                stack.append(num)

        return stack[0]