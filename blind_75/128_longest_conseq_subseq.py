from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest = 0

        for num in nums:

            current = 0

            if num - 1 not in nums_set:
                current = 1
                current_num = num
                while current_num + 1 in nums_set:
                    current += 1
                    current_num += 1

                longest = max(longest, current)

        return longest