# '' ''
# False

# 'a' ''
# True

# 'ab' 'acb'
# True

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if abs(len(s) - len(t)) > 1:
            return False

        def edit_dist(si, ti, used):
            if si == len(s) and ti == len(t):
                return used
            elif si == len(s) or ti == len(t):
                return not used

            if s[si] == t[ti]:
                return edit_dist(si + 1, ti + 1, used)
            else:
                if used:
                    return False
                else:
                    return edit_dist(si + 1, ti, True) or edit_dist(si, ti + 1, True) or edit_dist(si + 1, ti + 1, True)

        return edit_dist(0, 0, False)