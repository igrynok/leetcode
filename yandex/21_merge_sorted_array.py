# [0] [1] 0 1
# [1]

# [1] [] 1 0
# [1]

# [1, 2, 3, 0, 0, 0] [2, 5, 6]
# [1, 2, 2, 3, 5, 6]
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = m - 1, n - 1
        current = len(nums1) - 1

        while i2 >= 0:

            if i1 == -1:
                nums1[current] = nums2[i2]
                i2 -= 1
                current -= 1
                continue

            if nums1[i1] > nums2[i2]:
                nums1[current] = nums1[i1]
                i1 -= 1
            else:
                nums1[current] = nums2[i2]
                i2 -= 1

            current -= 1
