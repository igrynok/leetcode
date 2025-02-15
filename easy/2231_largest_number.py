from collections import deque

class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = str(num)
        even_digits = deque(sorted([d for d in num_str if int(d) % 2 == 0], reverse=True))
        odd_digits = deque(sorted([d for d in num_str if int(d) % 2 == 1], reverse=True))

        result = []
        for digit in num_str:
            if int(digit) % 2 == 0:
                result.append(even_digits.popleft())
            else:
                result.append(odd_digits.popleft())

        return int(''.join(result))