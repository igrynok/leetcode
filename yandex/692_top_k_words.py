from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        counter = Counter(words)
        word_counts = []

        for key in counter.keys():
            word_counts.append((counter[key], key))

        word_counts.sort(key = lambda x: (-x[0], x[1]))

        answer = []
        for i in range(k):
            answer.append(word_counts[i][1])

        return answer