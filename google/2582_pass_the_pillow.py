class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full_pass = time // (n - 1) + 1
        reminder = time % (n - 1)
        direction = full_pass % 2
        if direction == 1:
            return reminder + 1
        else:
            return n - reminder
