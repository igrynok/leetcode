# "ab"
# [1, 1]

# "eccbbbdec"
# [9]

# "abaede"
# [3, 3]

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        letter_map = {}
        for index, letter in enumerate(s):
            if letter not in letter_map:
                letter_map[letter] = index
            else:
                letter_map[letter] = index


        window = letter_map[s[0]]
        answer = []
        anchor = 0
        for index, letter in enumerate(s):
            window = max(letter_map[letter], window)
            if index == window:
                answer.append(index + 1 - anchor)
                anchor = index + 1

        return answer