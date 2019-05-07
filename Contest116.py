import bisect
import math


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        check = set()
        for elem in A:
            if elem in check:
                return elem
            else:
                check.add(elem)

    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        memo = [0]
        for i in range(1, len(A)):
            # DESC
            if A[i] < A[memo[-1]]:
                memo.append(i)
        refMemo = []
        memo = memo[::-1]
        for idx in memo:
            refMemo.append(A[idx])
        for j in range(1, len(A)):
            # find with DESC by binary search
            cur = bisect.bisect_right(refMemo, A[j])

            if cur > 0:
                i = cur - 1
                res = max(res, j - memo[i])
        return res

    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        # 等长 且等角度 且等
        # 边 角
        # 先找出所有等长等角度边？
        # 直角相乘为0
        # 平行向量相同 注意无向，所有vec = (a,b) a均 >=0
        # 所以先存储所有向量及其对应的出发点？
        # 向量n**2个 50个点 可行
        # 向量map垂直向量

        # remove duplicate point
        pSet = set()
        for point in points:
            pSet.add((point[0], point[1]))
        points = list(pSet)

        pDic = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a = points[i][0] - points[j][0]
                b = points[i][1] - points[j][1]
                # vec 属于 a>=0 (-90,90], 那么它的正交则永远为 b <= 0 (-180,0]
                start = points[j]
                end = points[i]
                if a < 0:
                    start = points[i]
                    end = points[j]
                    a = -a
                    b = -b
                elif a == 0 and b < 0:
                    start = points[i]
                    end = points[j]
                    b = -b

                if start not in pDic:
                    # 不可能重复
                    pDic[start] = [(a, b)]
                else:
                    pDic[start].append((a, b))
                # 有点没算清，算清应该不需要加end，提速一倍以上
                if end not in pDic:
                    # 不可能重复
                    pDic[end] = [(-a, -b)]
                else:
                    pDic[end].append((-a, -b))

        self.res = float('inf')
        searchL = []
        for key, val in pDic.items():
            if len(val) > 1:
                searchL.append(key)

        def search(p):
            for i in range(len(pDic[p])):
                for j in range(i + 1, len(pDic[p])):
                    if pDic[p][i][0] * pDic[p][j][0] + pDic[p][i][1] * pDic[p][j][1] == 0:
                        check((p[0] + pDic[p][i][0], p[1] + pDic[p][i][1]), pDic[p][i], pDic[p][j])

        def check(p, preO, preP):
            for cur in pDic[p]:
                if cur == preP and cur[0] * preO[0] + cur[1] * preO[1] == 0:
                    self.res = min(self.res,
                                   math.sqrt(cur[0] ** 2 + cur[1] ** 2) * math.sqrt(preO[0] ** 2 + preO[1] ** 2))

        for sp in searchL:
            search(sp)
        if self.res == float('inf'):
            self.res = 0
        return self.res

    def leastOpsExpressTargetSlow(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        if x == 1:
            return target - 1
        self.visited = {}

        def dfs(locT, last):
            if locT not in self.visited:
                print(locT)
                # we have 1 (x / x), x ** K, target进制？
                # 先无限连乘 直到比target大，min（cur+ func（multi-target）， cur - 1 + func（target-multi）
                # 最小单位为1， 除只是为了1
                if locT < 0:
                    return float('inf')
                elif locT == 0:
                    return -1
                elif locT == 1:
                    return 1
                elif x == locT:
                    return 0
                if x > locT:
                    return locT * 2 - 1
                count = 0
                nextV = x
                while nextV < locT:
                    nextV *= x
                    count += 1
                a = count + 1 + dfs(nextV - locT, locT) if nextV - locT != last else float('inf')
                b = count + dfs(locT - nextV / x, locT) if locT - nextV / x != last else float('inf')
                self.visited[locT] = min(a, b)
            return self.visited[locT]

        return dfs(target, float('inf'))

    def leastOpsExpressTargetBug(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        if x == 1:
            return target - 1
        self.visited = {}
        count = 0
        searchL = [target]
        nextL1 = []
        nextL2 = []
        while searchL:
            cur = searchL.pop(0)
            if cur == 1:
                return count + 1
            elif cur == x:
                return count
            else:
                memo = 0
                nextV = x
                while nextV < cur:
                    nextV *= x
                    memo += 1
                if nextV - cur == 0:
                    return count + memo
                else:
                    nextL2.append(nextV - cur)
                nextL1.append(cur - nextV / x)
            if not searchL:
                if not nextL2 and not nextL1:
                    return float('inf')
                print(nextL1, nextL2)
                # bug memo不同级
                count += memo
                searchL = nextL1
                nextL1 = nextL2
                nextL2 = []

    def leastOpsExpressTargetLittleBug(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """

        if x == 1:
            return target - 1
        if target == 0:
            return 0

        self.visited = {-1: [target]}

        while self.visited:
            print(sorted(self.visited))
            minKey = min(self.visited.keys())
            cur = self.visited[minKey].pop()
            if not self.visited[minKey]:
                del self.visited[minKey]
            if cur == 0:
                return minKey
            elif cur < x:
                self.visited[minKey + 2 * cur] = [0]
            else:
                memo = 0
                nextV = x
                while nextV < cur:
                    nextV *= x
                    memo += 1
                if nextV - cur == 0:
                    self.visited[minKey + memo + 1] = [0]
                else:
                    if minKey + memo + 1 not in self.visited:
                        self.visited[minKey + memo + 1] = [nextV - cur]
                    else:
                        self.visited[minKey + memo + 1].append(nextV - cur)
                    if minKey + memo not in self.visited:
                        self.visited[minKey + memo] = [cur - nextV / x]
                    else:
                        self.visited[minKey + memo].append(cur - nextV / x)
                memoM = cur // x
                if cur % x == 0:
                    self.visited[minKey + memoM] = [0]
                else:
                    if minKey + memoM + 1 not in self.visited:
                        self.visited[minKey + memoM + 1] = [x * (memoM+1) - cur]
                    else:
                        self.visited[minKey + memoM + 1].append(x * (memoM+1) - cur)
                    if minKey + memoM not in self.visited:
                        self.visited[minKey + memoM] = [cur - memoM * x]
                    else:
                        self.visited[minKey + memoM].append(cur - memoM * x)


A = Solution()
print(A.leastOpsExpressTarget(3, 60500045))
