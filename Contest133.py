# problem4

# slow version
class StreamCheckerOld(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.memo = [0 for _ in range(len(words))]
        self.words = words
        self.cur = ''

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.cur += letter

        def backtrack(pos, length):
            res = 0
            for i in range(length-1,0,-1):
                if self.cur[-i:] == self.words[pos][:i]:
                    res = i
                    break
            return res

        res = False
        for i in range(len(self.words)):
            if letter == self.words[i][self.memo[i]]:
                self.memo[i] += 1
                if self.memo[i] == len(self.words[i]):
                    res = True
                    self.memo[i] = backtrack(i, self.memo[i])
            else:
                self.memo[i] = backtrack(i, self.memo[i]+1)
        return res

# tri version0
class TriNode(object):
    def __init__(self):
        self.childs = {}
        self.isEnd = False

class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """

        self.tri = TriNode()
        self.maxL = 0
        for word in words:
            self.maxL = max(len(word),self.maxL)
            cur = self.tri
            for i in range(len(word)-1,-1,-1):
                if word[i] not in cur.childs:
                    cur.childs[word[i]] = TriNode()
                cur = cur.childs[word[i]]
            cur.isEnd = True
        self.str = ''

        #self.searchQ = set()
        #self.searchQ.add(self.tri)





    def query(self,letter):
        self.str += letter
        tri = self.tri
        for i in range(1,min(self.maxL,len(self.str))+1):
            if self.str[-i] in tri.childs:
                tri = tri.childs[self.str[-i]]
                if tri.isEnd:
                    return True
            else:
                break
        return False

    '''
    def queryOld(self, letter):
    """
    :type letter: str
    :rtype: bool
    """

    res = False
    newQ = set()
    for val in self.searchQ:
        if letter in val.childs:
            newQ.add(val.childs[letter])
            if val.childs[letter].isEnd:
                res = True
        self.searchQ = newQ
    return res
    '''


A = StreamChecker(["abaa","abaab","aabbb","bab","ab"])


for q in [["a"],["a"],["b"],["b"],["b"],["a"],["a"],["b"],["b"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["b"],["b"],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["a"],["b"],["b"],["b"],["a"],["b"],["a"]]:
    print(A.query(q[0]))
