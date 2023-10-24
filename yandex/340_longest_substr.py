class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = {}
        slow = 0
        longest_sub = 0

        for i, ch in enumerate(s):

            if ch in chars:
                chars[ch] += 1
            else:
                chars[ch] = 1

            while len(chars) > k:
                chars[s[slow]] -= 1
                if chars[s[slow]] == 0:
                    del chars[s[slow]]
                slow += 1

            longest_sub = max(longest_sub, i - slow + 1)

        return longest_sub