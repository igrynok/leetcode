# "abc" "ahbgdc"
# True

# "axc" "ahbgdc"
# False

# "a" ""
# False

# "" "a"
# True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s and not t:
            return True

        if not t:
            return False

        if not s:
            return True

        j = 0
        for i in range(len(t)):
            if s[j] == t[i]:
                if j == len(s) - 1:
                    return True
                else:
                    j += 1

        return False