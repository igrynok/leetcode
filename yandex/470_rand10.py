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
        space = [[1,2, 3, 4, 5, 6, 7], [8, 9, 10]]

        while True:
            num1 = rand7()
            num2 = rand7()

            if num2 == 1 or (num2 == 2 and num1 <= 3):
                return space[num2-1][num1-1]
