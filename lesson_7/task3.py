class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if not w in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = [self.root]
        for i, w in enumerate(word):
            newcur = []
            for node in cur:
                for key, value in node.children.items():
                    if w == '.' or w == key:
                        if i == len(word) - 1 and value.isWord:
                            return True
                        newcur.append(value)
            cur = newcur

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)