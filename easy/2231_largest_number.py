class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(map(int, str(num)))
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if num[i] % 2 == num[j] % 2 and num[j] > num[i]:
                    num[i], num[j] = num[j], num[i]

        return int(''.join(map(str, num)))