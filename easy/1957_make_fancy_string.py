class Solution:
    def makeFancyString(self, s: str) -> str:

        new_str = []
        index = 0
        while index < len(s):
            new_str.append(s[index])
            count = 1
            while index + count < len(s) and s[index] == s[index + count]:
                count += 1
            fix = index
            while count >= 3:
                count -= 1
                index += 1
            index += 1

        return "".join(new_str)