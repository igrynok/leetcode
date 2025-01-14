class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        minimal = str1 if len(str1) > len(str2) else str2

        for i in range(len(minimal), 0, -1):
            prefix = minimal[:i]
            if str1 == prefix*(len(str1)//len(prefix)) and str2 == prefix*(len(str2)//len(prefix)):
                return prefix

        return ""