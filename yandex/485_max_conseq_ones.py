class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max1s = 0
        current1s = 0

        for num in nums:

            if num == 1:
                current1s += 1
                max1s = max(max1s, current1s)
            else:
                current1s = 0

        return max1s