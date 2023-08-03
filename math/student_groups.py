import math


class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        total = len(grades)
        estimate = int(math.floor(math.sqrt(2*total)))

        group_nums = 0
        for i in range(1, estimate + 1):
            if total - i >= 0:
                group_nums += 1
                total -= i
            else:
                break

        return group_nums


if __name__ == '__main__':
    print(Solution().maximumGroups([10,6,12,7,3,5]))
