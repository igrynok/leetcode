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

        subs_set = set()
        max_subs = 0
        left = 0

        for right, ch in enumerate(s):
            if ch in subs_set:
                while ch in subs_set:
                    subs_set.remove(s[left])
                    left += 1
            subs_set.add(ch)

            max_subs = max(max_subs, right - left + 1)

        return max_subs