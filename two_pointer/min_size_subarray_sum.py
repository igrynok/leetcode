class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        if (len(nums) == 1 and nums[0] < target) or not nums:
            return 0

        if nums[0] >= target:
            return 1

        slow, fast = 0, 1
        current = nums[0] + nums[1]
        optimal = 10**6

        while (slow < len(nums) and fast < len(nums)):
            if current < target:
                fast += 1
                if fast < len(nums):
                    current += nums[fast]
            else:
                optimal = min(optimal, fast - slow + 1)
                current -= nums[slow]
                slow += 1

        return optimal if optimal != 10**6 else 0