class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [nums[0]]
        suffix = [nums[len(nums)-1]]

        for i in range(1, len(nums)):
            prefix.append(prefix[i-1]*nums[i])
            suffix.append(suffix[i-1]*nums[len(nums) - 1 - i])

        suffix = suffix[::-1]
        answer = [suffix[1]]
        for i in range(1, len(nums) - 1):
            answer.append(prefix[i - 1]*suffix[i + 1])
        answer.append(prefix[len(nums) - 2])

        return answer