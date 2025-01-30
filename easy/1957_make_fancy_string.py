class Solution:
    def makeFancyString(self, s: str) -> str:

        to_remove = []
        for index, elem in enumerate(s):
            if index >= len(s) - 2:
                break
            count = 1
            while count < 3:
                if elem != s[index + count]:
                    break
                count += 1
                if count == 3:
                    to_remove.append(index)

        return "".join([elem for index, elem in enumerate(s) if index not in to_remove])