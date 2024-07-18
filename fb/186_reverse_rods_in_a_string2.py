from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        if len(s) <= 1:
            return

        reverse(0, len(s) - 1)

        start, end = 0, 0
        while end + 1 < len(s):
            end += 1
            if s[end] == " ":
                reverse(start, end - 1)
                start, end = end + 1, end + 1
                continue

        reverse(start, end)
