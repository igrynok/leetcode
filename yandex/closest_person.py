# [1, 0]
# 1

# [0, 0, 1]
# 2

# [1, 0, 0, 0, 1, 0, 1]
# 2

class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:

        prev = -1
        max_dist = 0

        for i, seat in enumerate(seats):
            if seat == 1:
                if prev != -1:
                    max_dist = max(max_dist, (i - prev)//2)
                else:
                    max_dist = i
                prev = i

        max_dist = max(max_dist, len(seats) - prev - 1)

        return max_dist