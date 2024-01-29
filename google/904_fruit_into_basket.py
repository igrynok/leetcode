from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        if len(fruits) <= 2:
            return len(fruits)

        left, right = 0, 0
        left_type = fruits[0]

        index = 0
        while index < len(fruits) and fruits[index] == left_type:
            index += 1

        if index == len(fruits):
            return len(fruits)

        right_type = fruits[index]
        right = index

        basket_max = 0
        while right < len(fruits):

            while right + 1 < len(fruits) and (fruits[right + 1] == left_type or fruits[right + 1] == right_type):
                right += 1

            basket_max = max(basket_max, right - left + 1)

            left = right
            left_type = fruits[left]
            while left >= 1 and fruits[left - 1] == left_type:
                left -= 1

            right += 1
            if right < len(fruits):
                right_type = fruits[right]

        return basket_max
