class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        def dfs(index, sums):
            if index == len(cookies):
                return max(sums)

            if sum([1 for elem in sums if elem == 0]) > len(cookies) - index:
                return 10**8

            min_sum = 10**8
            for i in range(k):
                new_sums = sums[:]
                new_sums[i] += cookies[index]
                min_sum = min(dfs(index + 1, new_sums), min_sum)

            return min_sum

        sums = [0]*k
        return dfs(0, sums)


if __name__ == '__main__':
    cookies = [8,15,10,20,8]
    k = 2
    print(Solution().distributeCookies(cookies, k))