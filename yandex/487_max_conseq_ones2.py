# [1]
# 1

# [0]
# 1

# [1, 0, 1, 1, 0]
# 4

# [1, 0, 1, 1, 0, 1]
# 4


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        slow, fast = 0, 0
        zeros = 0
        longest = 0

        while fast < len(nums):

            if nums[fast] == 0:
                zeros += 1

            while zeros == 2:
                if nums[slow] == 0:
                    zeros -= 1
                slow += 1

            longest = max(longest, fast - slow + 1)
            fast += 1

        return longest