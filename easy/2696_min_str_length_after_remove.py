class Solution:
    def minLength(self, s: str) -> int:
        s_len = 0
        while True:
            if s_len == len(s):
                break
            s_len = len(s)
            for i in range(len(s) - 1):
                if "AB" == s[i:i+2] or "CD" == s[i:i+2]:
                    s = s[:i] + s[i+2:]
                    break
        return len(s)