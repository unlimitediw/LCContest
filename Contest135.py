class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import math


class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        if tuple(points[0]) == tuple(points[1]) or tuple(points[0]) == tuple(points[2]) or tuple(points[1]) == tuple(
                points[2]):
            return False
        v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        v2 = (points[2][0] - points[1][0], points[2][1] - points[1][1])
        if v1[1] == 0:
            if v2[1] == 0:
                return False
            else:
                return True
        if v2[1] == 0:
            if v1[1] == 0:
                return False
            else:
                return True

        if float(v1[0]) / float(v1[1]) == float(v2[0]) / float(v2[1]):
            return False
        return True

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(node, nodeR, preInh):
            res = nodeR.val
            node.val += preInh
            if nodeR.right:
                node.right = TreeNode(nodeR.right.val)
                curR = dfs(node.right, nodeR.right, preInh)
                res += curR
                node.val += curR
            if nodeR.left:
                node.left = TreeNode(nodeR.left.val)
                res += dfs(node.left, nodeR.left, node.val)
            return res

        newR = TreeNode(root.val)
        dfs(newR, root, 0)

        return newR

    # 原始边不可重复使用
    def minScoreTriangulationWithRepeated(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        visited = set()
        count = len(A) - 2
        res = 0
        while count > 0:
            minV = float('inf')
            curM = (-1, -1, -1)
            for i in range(len(A) - 1):
                for j in range(i + 1, len(A) - 1):
                    for k in range(j + 1, len(A) - 1):
                        cur = A[i] * A[j] * A[k]
                        if (i, j, k) not in visited:
                            if cur < minV:
                                curM = (i, j, k)
                                minV = cur
            visited.add(curM)
            res += minV
            count -= 1

        return res

    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # 不可sort, 每条边必须选一个点，先选的点会将问题分割成找两个子多边的最优解
        visited = {}

        def dfs(l, r, head):
            if l == r:
                return 0
            if (l, r, head) not in visited:
                curM = float('inf')
                for i in range(l + 1, r + 1):
                    curM = min(curM, A[head] * A[l] * A[i] + dfs(l + 1, i, l) + dfs(i, r, head))
                visited[(l, r, head)] = curM
            return visited[(l, r, head)]

        return dfs(1, len(A) - 1, 0)

    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """

        # 6 5 4 3 10
        stones.sort()
        pre = stones[0]
        preCount = 1
        memoS = []
        memoI = []
        for i in range(1, len(stones)):
            if stones[i] == pre + 1:
                pre += 1
                preCount += 1
            else:
                memoS.append(preCount)
                memoI.append(stones[i] - pre - 1)
                pre = stones[i]
                preCount = 1
        memoS.append(preCount)

        if len(memoI) == 0:
            return [0, 0]
        elif len(memoI) == 1:
            return [min(memoI[0], 2 * (min(memoS))), memoI[0]]
        else:
            if memoS[0] == 1 and memoS[-1] == 1:
                maxRes = sum(memoI) - min(memoI[0], memoI[-1])
            else:
                maxRes = sum(memoI)
            i = 0
            minRes = len(stones)
            for j in range(len(stones)):
                while stones[j] - stones[i] >= len(stones): i += 1
                if j - i + 1 == len(stones) - 1 and stones[j] - stones[i] == len(stones) - 2:
                    minRes = min(minRes, 2)
                else:
                    minRes = min(minRes, len(stones) - (j - i + 1))
            return [minRes, maxRes]

    def check(self, floor):
        answer = 73
        if floor == answer:
            return True
        return False

    # 不应该均分
    def superEggDrop(self, K, N):
        # minimum step to know which step break exactly
        # dp is used to keep which floor break?
        # dp = [[0 for _ in range(N)] for _ in range(K)]
        # if we know dp [K-1][N] can we know dp[K][N] ?
        # if we know dp [K][N-1] can we know dp[K][N] ?
        # obviously dp[0][0] = 1, dp[0][1] = 2 .... dp[0][n] = n - 1
        # When add one more egg, suppose divide sub problem to q floor check is optimal? find q
        # so we need to reconstruct dp , what we actually want is the optimal divided solution for add up
        # q = 1 to N, but actually stop at math.ceil(N/2)
        '''

        :param K:
        :param N:
        :return:
        '''

        # old version
        dp = [[0 for _ in range(N)] for _ in range(K)]
        curMin = N
        for i in range(N):
            dp[0][i] = i + 1
        for k in range(1, K):
            for n in range(1,N+1):
                minStep = N
                if n == 1:
                    dp[k][n - 1] = 1
                else:
                    for q in range(1, n+1):
                        minStep = min(minStep, int(math.ceil(float(n)/float(q + 1)) + dp[k - 1][q - 1]))
                    dp[k][n-1] = minStep
        for d in dp:
            show = []
            for i in d:
                show.append('{:2d}'.format(i))
            print(show)
        # differ from previous, dp[k][n][j] means we always guess with length N,but how many steps
        # we need to take if we spilt it to (j steps)
        '''
        dp = [[0 for _ in range(N)] for _ in range(K)]
        pre = float('inf')
        for i in range(N):
            dp[0][i] = min(i + int(math.ceil(N / (i + 1))) - 1, pre)
            pre = dp[0][i]
        '''
        return dp[K-1][N-1]


    def superEggDropRef(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = range(N + 1)
        for i in range(2, K + 1):
            q = 1
            ndp = [0, 1] + [float('inf')] * (N - 1)
            for j in range(2, N + 1):
                while q < j + 1 and ndp[j - q] > dp[q - 1]:
                    q += 1
                ndp[j] = 1 + dp[q - 1]
            dp = ndp
        return dp[N]
A = Solution()
print(A.superEggDropRef(100,10000))
