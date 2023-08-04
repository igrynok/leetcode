# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
# target value.
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(is_first):
            left, right = 0, len(nums) - 1
            first_index = -1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    first_index = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return first_index

        output = [-1, -1]

        first_index = binary_search(True)

        if first_index > -1:
            second_index = binary_search(False)
            output = [first_index, second_index]

        return output


if __name__ == '__main__':
    print(Solution().searchRange([1, 2, 3], 1))