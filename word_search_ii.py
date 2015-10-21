class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        trie = Trie()
        for w in words:
            trie.insert(w)
        width = len(board[0]); height  = len(board)
        visited = [ [False] * width for _ in range(height)]
        go = zip([ 1, 0, -1, 0], [0, 1, 0, -1])
        ans = []
        
        def dfs(word, node, x, y):
            node = node.childs.get(board[x][y])
            if node is None:
                return 
            visited[x][y] = True 
            for gg in go :
                nx, ny = x + gg[0], y+gg[1]
                if nx >= 0 and ny >= 0 and ny < width and nx <height and not visited[nx][ny]: 
                    dfs(word + board[nx][ny], node, nx, ny)
            if node.isWord:
                ans.append(word)
                trie.delete(word)
            visited[x][y] = False 
            
        
        for x in range(height):
            for y in range(width) :
                dfs(board[x][y], trie.root, x, y)
        return sorted(ans)
            
class TrieNode(object):
    def __init__(self):
        self.childs = {}
        self.isWord = False 
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True
        
    def delete(self, word):
        node = self.root
        queue = []
        for char in word:
            queue.append((char,node))
            child = node.childs.get(char)
            if not node:
                return False 
            node = child
        if not node.isWord:
            return False 
        if len(node.childs) : 
            node.isWord = False 
        else:
            for letter, node in reversed(queue):
                del node.childs[letter]
                if len(node.childs) or node.isWord:
                    break
        return True 

        