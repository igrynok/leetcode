class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if not digits:
            return [1]

        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            summed_digit = int(digit) + 1
            if summed_digit < 10:
                digits[i] = summed_digit
                return digits
            else:
                digits[i] = summed_digit%10
                if not i:
                    return [1] + digits

        return digits