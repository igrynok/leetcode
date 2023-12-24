class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        answer = []
        nums = list(range(1, n + 1))

        def dfs(path, index, k):
            if k == 0:
                answer.append(path[:])
                return
            for i in range(index, len(nums)):
                num = nums[i]
                path.append(num)
                dfs(path, i + 1, k - 1)
                path.pop()

        dfs([], 0, k)
        return answer