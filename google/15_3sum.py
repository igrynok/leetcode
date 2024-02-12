from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        num_dict = { num:i for i, num in enumerate(nums) }
        answer_set = set()
        answer = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum2 = -(nums[i] + nums[j])
                if sum2 in num_dict and num_dict[sum2] > i and num_dict[sum2] > j:
                    candidate = [nums[i], nums[j], nums[num_dict[sum2]]]
                    cand_sorted = tuple(sorted(candidate))
                    if not cand_sorted in answer_set:
                        answer_set.add(cand_sorted)
                        answer.append(candidate)

        return answer