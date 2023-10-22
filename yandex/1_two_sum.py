# [2, 7, 11, 15], 9
# [0, 1]

# [3, 3], 6
# [0, 1]

# [3, 2, 4]
# [1, 2]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dict = {}

        for index, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target-num], index]
            else:
                num_dict[num] = index

        return None