# ['a'] - > ['a']
# 1

# [a, a, b, b, c, c, c] - > [a2b2c3]
# 6

# [a, b, b, b, b, b, b, b, b, b ,b, b, b] - > [ab12]
# 4

class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0
        slow = 0

        while i < len(chars):

            ch = chars[i]
            chars[slow] = ch
            slow += 1
            count = 1

            while i + 1 < len(chars) and chars[i + 1] == ch:
                count += 1
                i += 1

            if count != 1:
                for s in str(count):
                    chars[slow] = s
                    slow += 1

            i += 1

        return slow