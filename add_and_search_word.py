
class TrieNode(object):
    def __init__(self ) :
        self.children = dict()
        self.isWord = False 
        
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            child = node.children.get(char)
            if child == None:
                child = TrieNode()
                node.children[char] = child
            node = child
        node.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root, word)
        
    # recursion
    def find(self, node, word):
        if word == '' :
            return node.isWord
        if word[0] == "." :
            for x in node.children:
                if self.find(node.children[x], word[1:]):
                    return True
        else:
            child = node.children.get(word[0])
            if child:
                return self.find( child, word[1:])
        return False 
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")