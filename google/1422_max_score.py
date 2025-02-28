class Solution:
    def maxScore(self, s: str) -> int:

        total = sum([int(ch) for ch in s])
        max_sum = 0
        zeros = 0

        for ch in s[:-1]:
            if ch == '0':
                zeros += 1
            else:
                total -= 1

            max_sum = max(max_sum, zeros + total)

        return max_sum
