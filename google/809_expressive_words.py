from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def get_dict(word):

            ch = word[0]
            word_count = 0
            letters = []
            counts = []

            for i, char in enumerate(word):
                if char == ch:
                    word_count += 1
                    continue
                else:
                    letters.append(ch)
                    counts.append(word_count)
                    ch = char
                    word_count = 1
            letters.append(ch)
            counts.append(word_count)

            return letters, counts

        letters_s, counts_s = get_dict(s)
        count = 0

        for word in words:
            letters_word, counts_word = get_dict(word)
            good_word = True

            if len(letters_s) != len(letters_word):
                continue

            for i, letter in enumerate(letters_s):
                if letters_word[i] != letter:
                    good_word = False
                    break
                s_count = counts_s[i]
                word_count = counts_word[i]
                if (s_count == 1 and word_count == 1) or (s_count == 2 and word_count == 2) or (s_count > 2 and s_count >= word_count):
                    continue
                else:
                    good_word = False
                    break
            if good_word:
                count += 1

        return count