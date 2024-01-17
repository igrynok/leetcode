from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        logs.sort()
        friends_groups = []

        for log in logs:

            f1, f2 = log[1], log[2]
            f1_group, f2_group = None, None

            for group in friends_groups:
                if f1 in group:
                    f1_group = group
                if f2 in group:
                    f2_group = group

            if not f1_group and not f2_group:
                friends_groups.append({f1, f2})
            elif f1_group and f2_group:
                if f1_group is not f2_group:
                    union = f1_group.union(f2_group)
                    friends_groups.remove(f1_group)
                    friends_groups.remove(f2_group)
                    friends_groups.append(union)
            elif f1_group:
                f1_group.add(f2)
            elif f2_group:
                f2_group.add(f1)

            if len(friends_groups) == 1 and len(friends_groups[0]) == n:
                return log[0]

        return -1