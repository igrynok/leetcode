# [0]
# 0

# [1]
# [0]

# [1, 1, 0, 1]
# 3

# [0, 1, 1, 1, 0, 1, 1, 0, 1]
# 5

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        zipped = []
        count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                if count > 0:
                    zipped.append(count)
                    count = 0
                zipped.append(num)

        if count > 0:
            zipped.append(count)

        if len(zipped) == 0:
            return 0

        if len(zipped) == 1:
            return zipped[0] - 1 if zipped[0] != 0 else 0

        max_count = max(zipped)

        cur_num = 0
        for i, num in enumerate(zipped):
            if num != 0:
                cur_num = num
            else:
                if cur_num != 0 and i + 1 < len(zipped) and zipped[i + 1] != 0:
                    max_count = max(max_count, cur_num + zipped[i + 1])
                else:
                    cur_num = 0

        return  max_count