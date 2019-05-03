class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        cur = ''
        for c in A:
            cur += str(c)
        cur = int(cur)
        cur += K
        cur = str(cur)
        res = []
        for i in range(len(cur)):
            res.append(int(cur[i]))
        return res

    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        visited = set()
        checkList = []
        memoList = []
        posDic = {}
        for i in range(len(equations)):
            if equations[i][1] == '!':
                checkList.append(equations[i])
            else:
                memoList.append(equations[i])
                memoList.append(equations[i][::-1])
        for i in range(len(memoList)):
            if memoList[i][0] not in posDic:
                posDic[memoList[i][0]] = [i]
            else:
                posDic[memoList[i][0]].append(i)
        checkers = []
        for i in range(len(memoList)):
            if memoList[i][0] not in visited:
                start = memoList[i][0]
                totalSet = {start}
                curSet = {start}
                visited.add(start)
                while curSet:
                    nextSet = set()
                    for cur in curSet:
                        if cur in posDic:
                            visited.add(cur)
                            for idx in posDic[cur]:
                                if memoList[idx][3] not in visited:
                                    nextSet.add(memoList[idx][3])
                    totalSet |= nextSet
                    curSet = nextSet
                checkers.append(totalSet)
        for check in checkList:
            if check[0] == check[3]:
                return False
            for checker in checkers:
                if check[0] in checker and check[3] in checker:
                    return False
        return True

    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        # double之后溢出k， 减位double之后溢出k-2，问题在于，没溢出之前也不应该一直double。后者说，正常来说倍数之前，一半是目标，或者加一一半
        if X >= Y:
            return X - Y
        if Y % 2 == 1:
            return self.brokenCalc(X,Y+1) + 1
        opti = self.brokenCalc(X, Y // 2) + 1
        return opti

    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        left = 0
        right = 0
        for i in range(len(A))