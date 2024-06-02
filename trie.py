class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.end = True

    def search(self, word: str) -> bool:
        node = self.__searchHelper(word)
        if not node:
            return False
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.__searchHelper(prefix)
        if not node:
            return False
        return True

    def __searchHelper(self, prefix):
        cur = self.root
        for letter in prefix:
            if not cur:
                return
            if letter not in cur.children:
                return
            cur = cur.children[letter]
        return cur
