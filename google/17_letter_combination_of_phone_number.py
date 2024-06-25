from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        phone_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        answer = []

        def dfs(index, path):
            if index == len(digits):
                answer.append("".join(path[:]))
                return

            letter = digits[index]
            for ch in phone_dict[letter]:
                path.append(ch)
                dfs(index + 1, path)
                path.pop()

        dfs(0, [])

        return answer
