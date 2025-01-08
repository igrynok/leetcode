class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            for j in range(len(goal)):
                if i + j < len(s):
                    if goal[j] == s[i + j]:
                        if j == len(goal) - 1:
                            return True
                        else:
                            continue
                    else:
                        break
                else:
                    if goal[j] == s[i + j - len(s)]:
                        if j == len(goal) - 1:
                            return True
                        else:
                            continue
                    else:
                        break

        return False