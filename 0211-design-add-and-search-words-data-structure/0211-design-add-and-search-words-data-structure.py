class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        def fun(node, wrd):
            if not wrd:
                return node.isWord

            c = wrd[0]
            remaining_word = wrd[1:]

            if c == '.':
                for child in node.children.values():
                    if fun(child, remaining_word):
                        return True
                return False
            else:
                if c in node.children:
                    return fun(node.children[c], remaining_word)
                else:
                    return False

        return fun(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)