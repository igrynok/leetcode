from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        answer = []
        count_nums1 = Counter(nums1)

        for num2 in nums2:
            if num2 in count_nums1:
                if count_nums1[num2] > 0:
                    count_nums1[num2] -= 1
                    answer.append(num2)

        return answer