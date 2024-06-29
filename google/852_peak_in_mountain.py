from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left, right = 0, len(arr)
        while left <= right:
            mid = (left + right)//2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid

        return -1