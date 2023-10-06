class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if(len(s) == 0):
            return True

        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

        s = s.lower()

        to_remove = []
        for ch in s:
            if ch not in alphabet:
                to_remove.append(ch)

        for ch in to_remove:
            s = s.replace(ch, "")

        if s == s[::-1]:
            return True

        return False