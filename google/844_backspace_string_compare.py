class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def normalize(s):
            norm = []
            skip = 0
            for elem in s[::-1]:
                if elem == "#":
                    skip += 1
                    continue
                else:
                    if skip > 0:
                        skip -= 1
                        continue
                    else:
                        norm.append(elem)

            return ''.join(norm)

        return  normalize(s) == normalize(t)