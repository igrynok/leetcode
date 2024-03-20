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

        slow = 0
        min_subs = ""

        for fast in range(len(s)):

            if s[fast] in counter.keys():
                counter[s[fast]] -= 1

            if self.is_empty(counter):
                for slow_i in range(slow, fast + 1):
                    if s[slow_i] in counter.keys() and counter[s[slow_i]] < 0:
                        counter[s[slow_i]] += 1
                    elif not s[slow_i] in counter.keys():
                        continue
                    else:
                        slow = slow_i
                        break

                if not min_subs or len(min_subs) > fast - slow + 1:
                    min_subs = s[slow:fast + 1]

        return min_subs