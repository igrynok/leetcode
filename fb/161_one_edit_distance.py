class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def is_one_eidt_distance(i, j, used):
            if i == len(s) and j == len(t):
                return used

            if j == len(t):
                if not used:
                    return is_one_eidt_distance(i + 1, j, True)
                return False

            if i == len(s):
                if not used:
                    return is_one_eidt_distance(i, j + 1, True)
                return False

            if s[i] == t[j]:
                return is_one_eidt_distance(i + 1, j + 1, used)
            else:
                if used:
                    return False
                else:
                    return is_one_eidt_distance(i + 1, j, True) or is_one_eidt_distance(i + 1, j + 1, True) or is_one_eidt_distance(i, j + 1, True)

        if not s and not t:
            return False

        return is_one_eidt_distance(0, 0, False)