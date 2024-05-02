class Solution:
    def __init__(self):
        self.index = 0

    def decodeString(self, s: str) -> str:

        result = ''

        while self.index < len(s) and s[self.index] != ']':
            if not s[self.index].isnumeric():
                result += s[self.index]
                self.index += 1
            else:
                k = 0
                while self.index < len(s) and s[self.index].isnumeric():
                    k = k*10 + int(s[self.index])
                    self.index += 1
                self.index += 1
                decoded = self.decodeString(s)
                result += decoded*k
                self.index += 1

        return result