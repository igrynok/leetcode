class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        left, right = 0, len(nums) - 1
        breaking_point = -1

        if nums[-1] < nums[0]:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    breaking_point = mid
                    right = mid - 1

        left, right = 0, len(nums) - 1
        if breaking_point > -1:
            if target <= nums[-1]:
                left, right = breaking_point, len(nums) - 1
            else:
                left, right = 0, breaking_point

        search_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                search_index = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return search_index


if __name__ == '__main__':
    print(Solution().search([3, 1], 1))
