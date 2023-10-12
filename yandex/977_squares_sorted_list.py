# [2]
# [4]

# [1, 3]
# [1, 9]

# [-3, 2]
# [4, 9]

# [-4, -1, 0, 3, 10]
# [0, 1, 9, 16, 100]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        squares = [-1]*len(nums)

        left, right = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[left]**2 >= nums[right]**2:
                squares[i] = nums[left]**2
                left += 1
            else:
                squares[i] = nums[right]**2
                right -= 1

        return squares
