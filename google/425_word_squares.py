from collections import defaultdict
from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        prefix_dict = defaultdict(list)
        prefix_dict[''] = [word for word in words]

        for word in words:
            for i in range(len(word) - 1):
                prefix_dict[word[:i+1]].append(word)

        answer = []
        word_len = len(words[0])

        def dfs(prefix, chain):
            if len(prefix) == word_len:
                answer.append(chain[:])
                return

            i = len(prefix) + 1
            for word in prefix_dict[prefix]:
                chain.append(word)
                if i < word_len:
                    new_prefix = ''.join([w[i] for w in chain])
                else:
                    new_prefix = word
                dfs(new_prefix, chain)
                chain.pop()

        dfs("", [])

        return answer