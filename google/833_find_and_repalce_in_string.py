from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        origin = list(s)

        for i, source in enumerate(sources):
            index = indices[i]
            if s[index:index + len(source)] == source:
                origin[index] = targets[i]
                for i in range(index + 1, index + len(source)):
                    origin[i] = ''

        return ''.join(origin)