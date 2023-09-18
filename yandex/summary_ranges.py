class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return nums

        i = 0
        result = []
        while i < len(nums):
            start = nums[i]
            while (i + 1) < len(nums) and nums[i+1] - nums[i] == 1:
                i += 1
            if start != nums[i]:
                result.append(str(start) + "->" + str(nums[i]))
            else:
                result.append(str(start))
            i += 1

        return result