class Trie:

    def __init__(self):
        self.root = {}


    def insert(self, word: str) -> None:

        node = self.root
        for ch in word:
            if ch not in node.keys():
                node[ch] = {}
            node = node[ch]
        node['*'] = ''

    def search(self, word: str) -> bool:

        node = self.root
        for ch in word:
            if ch not in node.keys():
                return False
            node = node[ch]

        return '*' in node.keys()

    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for ch in prefix:
            if ch not in node.keys():
                return False
            node = node[ch]

        return True