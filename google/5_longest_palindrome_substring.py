class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[False]*len(s) for i in range(len(s))]
        start, end = 0, 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j] and j - i > end - start:
                    start = i
                    end = j

        return s[start:end + 1]      