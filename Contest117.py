class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TriNode(object):
    def __init__(self, x):
        self.val = x
        self.sub = {}
        self.end = 0


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        self.val = root.val

        def check(node):
            if not node:
                return True
            elif node.val != self.val:
                return False
            else:
                return check(node.left) and check(node.right)

        return check(root)

    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        visited = {}

        def check(head, length):
            if length == 1:
                return str(head)
            if (head, length) not in visited:
                res = []
                headRes = []
                if head + K < 10:
                    res += check(head + K, length - 1)
                if head - K > -1:
                    res += check(head - K, length - 1)
                for s in res:
                    headRes.append(str(head) + s)
                visited[(head, length)] = headRes
            return visited[(head, length)]

        final = []
        for i in range(1, 10):
            final += check(i, N)
        for i in range(len(final)):
            final[i] = int(final[i])
        if N == 1:
            final.append(0)
        if K == 0:
            return list(set(final))
        return final

    def spellcheckerSlow(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        checkSet = set(wordlist)
        res = []

        def matchVowel(word, query, keyPos):
            if len(word) != len(query):
                return False
            word = word.lower()
            for i in range(len(word)):
                if i not in keyPos:
                    if word[i] != query[i]:
                        return False
                else:
                    if word[i] not in {'a', 'e', 'i', 'o', 'u'}:
                        return False
            return True

        for query in queries:
            if query in checkSet:
                res.append(query)
            else:
                query = query.lower()
                keyPos = []
                for i in range(len(query)):
                    if query[i] in {'a', 'e', 'i', 'o', 'u'}:
                        keyPos.append(i)
                keyPos = set(keyPos)
                find = False
                for i in range(len(wordlist)):
                    if wordlist[i].lower() == query:
                        res.append(wordlist[i])
                        find = True
                        break
                if not find:
                    for i in range(len(wordlist)):
                        if matchVowel(wordlist[i], query, keyPos):
                            res.append(wordlist[i])
                            find = True
                            break
                if not find:
                    res.append('')
        return res

    # Trie
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        check = set(wordlist)
        root = TriNode('')
        for idx in range(len(wordlist)):
            word = wordlist[idx].lower()
            cur = root
            for i in range(len(word)):
                if word[i] not in cur.sub:
                    cur.sub[word[i]] = TriNode(word[i])
                    if i == len(word) - 1:
                        cur.sub[word[i]].end = idx + 1
                cur = cur.sub[word[i]]

        def find(q):
            if not q:
                return ''
            # loop 1,
            solo = root
            pos = 0
            while pos != len(q):
                if q[pos] in solo.sub:
                    if pos == len(q) - 1 and solo.sub[q[pos]].end:
                        return wordlist[solo.sub[q[pos]].end - 1]
                    solo = solo.sub[q[pos]]
                    pos += 1
                else:
                    break
            search = [root]
            nextSearch = []
            res = []
            pos = 0
            while search:
                cur = search.pop()
                qpList = [q[pos]]
                if q[pos] in {'a', 'e', 'i', 'o', 'u'}:
                    qpList = ['a', 'e', 'i', 'o', 'u']
                for qp in qpList:
                    if qp in cur.sub:
                        if pos == len(q) - 1 and cur.sub[qp].end:
                            res.append(cur.sub[qp].end)
                        nextSearch.append(cur.sub[qp])
                if not search:
                    pos += 1
                    search = nextSearch
                    nextSearch = []
                    if pos == len(q):
                        break
            if res:
                return wordlist[min(res) - 1]
            return ''

        final = []
        for query in queries:
            if query in check:
                final.append(query)
            else:
                query = query.lower()
                final.append(find(query))
        return final

    def minCameraCoverOld(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def count(node):
            # num_of_pre, do_you_need
            if not node.left and not node.right:
                return 0
            left = 1
            right = 1
            if node.left:
                left = count(node.left)
            if node.right:
                right = count(node.right)
            need = min(left, right)
            if need == -1:
                self.res += 1
                return 1
            elif need == 0:
                return -1
            else:
                return 0

        cur = count(root)
        if cur == -1 or cur == 0:
            self.res += 1
        return max(self.res, 1)

    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def count(node):
            if not node:
                return False, True
            lCam, lCov = count(node.left)
            rCam, rCov = count(node.right)

            cov = False
            cam = False

            if lCam or rCam:
                cov = True
            if not lCov or not rCov:
                cam = True
                cov = True
                self.res += 1
            return cam, cov

        rootCov = count(root)[1]
        if not rootCov:
            self.res += 1
        return self.res


A = Solution()
p = TreeNode(0)
p.left = TreeNode(0)
p.left.left = TreeNode(0)
p.left.left.left = TreeNode(0)
p.left.left.left.right = TreeNode(0)
print(A.minCameraCover(p))
