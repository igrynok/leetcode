from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def bt(arr, counter):
            if len(arr) == len(nums):
                answer.append(arr[:])
                return

            for num in counter:
                if counter[num] > 0:
                    arr.append(num)
                    counter[num] -= 1
                    bt(arr, counter)
                    arr.pop()
                    counter[num] += 1

        counter = Counter(nums)
        bt([], counter)
        return answer
