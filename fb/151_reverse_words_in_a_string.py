class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        reversed_word = []
        for i in range(len(arr) - 1, -1, -1):
            reversed_word.append(arr[i])

        return " ".join(reversed_word)