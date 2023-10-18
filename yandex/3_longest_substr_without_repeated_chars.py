# "abcabcbb"
# 3

# ""
# 0

# "bbbbb"
# 1

# "pwwkew"
# 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        slow, fast = 0, 0
        max_sub = 0
        letters = set()

        while fast < len(s):

            while fast < len(s) and not s[fast] in letters:
                letters.add(s[fast])
                fast += 1

            max_sub = max(max_sub, fast - slow)

            if fast == len(s):
                return max_sub

            repeated_letter = s[fast]

            while s[slow] != repeated_letter:
                letters.remove(s[slow])
                slow += 1

            letters.remove(s[slow])
            slow += 1

        return max_sub