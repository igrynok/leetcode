# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
# target value. 
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left, right = 0, len(nums) - 1
        first_index = -1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                first_index = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        output = [-1, -1]

        if first_index > -1:

            second_index = first_index

            for i in range(first_index, len(nums)):
                if nums[i] == target:
                    second_index = i
                else:
                    break

            output = [first_index, second_index]

        return output


if __name__ == '__main__':
    print(Solution().searchRange([1, 2, 3], 1))