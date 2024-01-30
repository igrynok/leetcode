from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        if len(fruits) <= 2:
            return len(fruits)

        basket = defaultdict(int)
        left = 0
        max_num = 0

        for right in range(len(fruits)):

            basket[fruits[right]] += 1

            if len(basket) > 2:
                while len(basket) > 2:
                    basket[fruits[left]] -= 1
                    if basket[fruits[left]] == 0:
                        del basket[fruits[left]]
                    left += 1

            max_num = max(max_num, right - left + 1)

        return max_num 