class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        index = 0
        i = 0
        while i < len(abbr):
            if index >= len(word):
                return False
            if abbr[i].isalpha():
                if abbr[i] == word[index]:
                    index += 1
                    i += 1
                else:
                    return False
            else:
                num = abbr[i]
                if num == '0':
                    return False
                while i + 1 < len(abbr) and abbr[i + 1].isdigit():
                    num += abbr[i + 1]
                    i += 1
                num = int(num)
                if index + num - 1 < len(word):
                    index = index + num
                    i += 1
                else:
                    return False

        return True if index == len(word) else False