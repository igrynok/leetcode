# "a"
# "a"

# "babad"
# "bab"

# "cbbd"
# "bb"

class Solution:

    def is_palindrome(self, word, start, end):

        while start <= end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1

        return True

    def longestPalindrome(self, s: str) -> str:

        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    if j - i + 1 > len(longest):
                        longest = s[i:j + 1]
                    if len(longest) == len(s):
                        return longest

        return longest