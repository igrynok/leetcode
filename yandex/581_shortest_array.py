# [2]
# 0

# [1, 2, 3, 4]
# 0

# [2, 6, 4, 8, 10, 9, 15]
# 5

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        nums_sorted = sorted(nums)

        low_index = -1
        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                low_index = i
                break

        high_index = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != nums_sorted[i]:
                high_index = i
                break

        return high_index - low_index + 1 if low_index != -1 else 0