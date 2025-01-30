class Solution:
    def makeFancyString(self, s: str) -> str:

        to_remove = []

        index = 0
        while index < len(s) - 2:
            count = 1
            while index + count < len(s) and s[index] == s[index + count]:
                count += 1
            fix = index
            while count >= 3:
                to_remove.append(fix + count - 1)
                count -= 1
                index += 1
            index += 1

        return "".join([elem for index, elem in enumerate(s) if index not in to_remove])