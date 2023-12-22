class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        self.answer = False

        @cache
        def dfs(start):
            if start == len(s):
                self.answer = True
                return
            for i in range(start + 1, len(s) + 1):
                if s[start:i] in word_set:
                    dfs(i)

        dfs(0)

        return self.answer