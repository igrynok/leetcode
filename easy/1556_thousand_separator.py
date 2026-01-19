class Solution:
    def thousandSeparator(self, n: int) -> str:
        str_n = str(n)[::-1]
        result = ""
        for i in range(0, len(str_n), 3):
            result += str_n[i:i + 3]
            if i + 3 < len(str_n):
                result += "."
        return result[::-1]