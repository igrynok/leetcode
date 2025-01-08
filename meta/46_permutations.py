from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        outcome = []

        def bt(arr):
            if len(arr) == len(nums):
                outcome.append(arr[:])

            for num in nums:
                if num not in arr:
                    arr.append(num)
                    bt(arr)
                    arr.pop()

        bt([])
        return outcome
