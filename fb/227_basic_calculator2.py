class Solution:
    def calculate(self, s: str) -> int:

        operation = '+'
        number = ''
        stack = []

        i = 0
        while i < len(s):
            if s[i].isnumeric():
                number += s[i]
                while i + 1 < len(s) and s[i + 1].isnumeric():
                    number += s[i + 1]
                    i += 1
                if operation == '+':
                    stack.append(int(number))
                elif operation == '-':
                    stack.append(-int(number))
                elif operation == '*':
                    stack.append(stack.pop()*int(number))
                elif operation == '/':
                    stack.append(int(stack.pop()/int(number)))
            elif s[i] == ' ':
                i += 1
                continue
            else:
                operation = s[i]
                number = ''
            i += 1

        return sum(stack)