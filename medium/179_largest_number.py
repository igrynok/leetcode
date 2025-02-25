class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums_str = [str(num) for num in nums]
        nums_str.sort(reverse=True, key=lambda x: x * 9)

        if nums_str[0] == "0":
            return "0"

        return "".join(nums_str)