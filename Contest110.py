class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        memoDic = {}
        strList = []
        digList = []
        # to list mode
        for logStr in logs:
            curStr = ''
            for i in range(len(logStr)):
                if logStr[i] == ' ':
                    curStr = logStr[i + 1:]
                    break
            if 47 < ord(curStr[0]) < 58:
                digList.append(curStr)
            else:
                strList.append(curStr)
            if curStr not in memoDic:
                memoDic[curStr] = [logStr]
            else:
                memoDic[curStr].append(logStr)
        strList.sort()
        res = strList + digList
        finalRes = []
        for elem in res:
            finalRes += memoDic[elem]
        return finalRes

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        self.total = 0

        def addVal(node):
            if not node:
                return
            if L <= node.val <= R:
                self.total += node.val
                addVal(node.left)
                addVal(node.right)
            elif node.val < L:
                addVal(node.right)
            else:
                addVal(node.left)

        addVal(root)
        return self.total

    def minAreaRectOld(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        horiDic = {}
        vertiDic = {}

        for point in points:
            if point[0] not in vertiDic:
                vertiDic[point[0]] = [point[1]]
            else:
                vertiDic[point[0]].append(point[1])
            if point[1] not in horiDic:
                horiDic[point[1]] = [point[0]]
            else:
                horiDic[point[1]].append(point[0])

        minArea = float('inf')


    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        ysforx = defaultdict(set)

        for x, y in points:
            ysforx[x].add(y)

        ans = 10 ** 100

        keys = sorted(ysforx)
        n = len(keys)
        for i in range(n):
            for j in range(i + 1, n):
                ps = ysforx[keys[i]] & ysforx[keys[j]]
                ps = sorted(ps)
                mindiff = 10 ** 100
                for x, y in zip(ps, ps[1:]):
                    mindiff = min(mindiff, y - x)
                if mindiff < 10 ** 100:
                    ans = min(ans, (keys[j] - keys[i]) * mindiff)

        return ans if ans < 10 ** 100 else 0
A = Solution()
t = TreeNode(3)
t.left = TreeNode(1)
t.right = TreeNode(5)
print(A.rangeSumBST(t,0,4))
print(A.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
