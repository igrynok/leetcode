# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to

def rand7():
    pass


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:

            col = rand7()
            row = rand7()

            num = (row - 1) * 7 + col

            if num <= 40:
                break

        return num % 10 + 1
