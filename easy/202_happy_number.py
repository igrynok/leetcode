class Solution:
    def isHappy(self, n: int) -> bool:

        num_set = set()
        while n not in num_set:
            num_set.add(n)
            n = sum([int(digit) ** 2 for digit in str(n)])
            if n == 1:
                return True

        return False
