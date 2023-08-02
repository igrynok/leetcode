from collections import deque


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        queue = deque([[num] for num in nums])

        while len(queue) > 0:

            if len(queue[0]) == 3:
                break

            node = queue.popleft()

            for num in nums:
                if num in node:
                    continue
                new_node = node[:]
                new_node.append(num)
                queue.append(new_node)

        return list(queue)


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
