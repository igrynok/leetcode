from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(current, count):
            if current > amount:
                return 10**9
            if current == amount:
                return count
            min_coins = 10**9
            for coin in coins:
                min_coins = min(min_coins, dfs(current + coin, count + 1))
            return min_coins

        result = dfs(0, 0)
        return result if result != 10**9 else -1