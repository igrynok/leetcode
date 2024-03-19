from collections import defaultdict, Counter


class Solution:

    def is_empty(self, dict):
        for key in dict.keys():
            if dict[key] > 0:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:

        counter = defaultdict(int)
        counter.update(Counter(t))
        slow, fast = 0, 0
        min_subs = ""

        while fast < len(s):

            if s[fast] in counter.keys():
                counter[s[fast]] -= 1

            if self.is_empty(counter):
                if not min_subs or len(min_subs) > fast - slow + 1:
                    min_subs = s[slow:fast+1]
                counter[s[slow]] += 1
                slow += 1
                while slow < fast and not s[slow] in counter.keys():
                    slow += 1
                counter[slow] -= 1

            fast += 1

        return min_subs