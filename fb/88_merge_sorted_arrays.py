class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        last1 = m - 1
        last2 = n - 1
        last = len(nums1) - 1

        while last2 >= 0:

            if last1 < 0:
                nums1[last] = nums2[last2]
                last2 -= 1
            elif nums1[last1] > nums2[last2]:
                nums1[last] = nums1[last1]
                last1 -= 1
            else:
                nums1[last] = nums2[last2]
                last2 -= 1

            last -= 1