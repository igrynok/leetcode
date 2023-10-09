# [1], k=1, x=-1
# 1

# [1, 2, 3, 4, 5], k=4, x=3
# [1, 2, 3, 4]

# [1, 2, 3, 4, 5] k=4, x=-1
# [1, 2, 3, 4]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        diff = 10**9
        index = -1

        for i, elem in enumerate(arr):
            if abs(x - elem) < diff:
                diff = abs(x - elem)
                index = i

        left, right = index, index
        while right - left < k - 1:
            if left - 1 >= 0 and right + 1 < len(arr):
                if abs(x - arr[left - 1]) <=  abs(x - arr[right + 1]):
                    left -= 1
                else:
                    right += 1
            elif left - 1 < 0:
                right += 1
            elif right + 1 >= len(arr):
                left -= 1

        return arr[left:right + 1]