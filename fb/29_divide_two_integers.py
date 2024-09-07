class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        count = 0
        sum = 0

        while True:
            sum += divisor
            if sum > dividend:
                return count
            else:
                count += 1

        return count