class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        j = 0
        result = []
        i_turn = True

        while i < len(word1) or j < len(word2):
            if i < len(word1) and i_turn or j >= len(word2):
                result.append(word1[i])
                i += 1
                i_turn = False
            else:
                result.append(word2[j])
                j += 1
                i_turn = True

        return ''.join(result)