class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answer = []

        def dfs(used, seq):

            if sum(used) == 0:
                answer.append(seq[:])
                return

            for index, elem in enumerate(used):
                if elem == 0:
                    continue
                if index == 0:
                    first_index = seq.index(0)
                    seq[first_index] = 1
                    used[0] = 0
                    dfs(used, seq)
                    used[0] = 1
                    seq[first_index] = 0
                else:
                    num = index + 1
                    first_index = seq.index(0)
                    last_index = first_index + num
                    if last_index >= 1 + (n - 1) * 2 or seq[last_index] != 0:
                        continue
                    used[index] = 0
                    seq[first_index] = num
                    seq[last_index] = num
                    dfs(used, seq)
                    used[index] = 1
                    seq[first_index] = 0
                    seq[last_index] = 0

        used = [1] * n
        seq = [0] * (1 + (n - 1) * 2)
        dfs(used, seq)
        return max(answer)


if __name__ == '__main__':
    print(Solution().constructDistancedSequence(3))
