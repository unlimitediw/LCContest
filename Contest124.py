import math


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        self.xD = -1
        self.yD = -1
        self.xP = -1
        self.yP = -1

        def search(node, depth, parent):
            if node.val == x:
                self.xD = depth
                self.xP = parent
            if node.val == y:
                self.yD = depth
                self.yP = parent
            if node.left:
                search(node.left, depth + 1, node.val)
            if node.right:
                search(node.right, depth + 1, node.val)

        search(root, 0, float('inf'))

        return self.xD == self.yD and self.xP != self.yP

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.remain = 0
        count = 0
        cur = []
        next = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.remain += 1
                if grid[i][j] == 2:
                    cur.append((i, j))
        if self.remain == 0:
            return 0
        if not cur:
            return -1

        def check(pos):
            if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                if grid[pos[0]][pos[1]] == 1:
                    grid[pos[0]][pos[1]] = 2
                    next.append((pos[0], pos[1]))
                    self.remain -= 1

        while True:
            rotten = cur.pop()
            check((rotten[0] + 1, rotten[1]))
            check((rotten[0] - 1, rotten[1]))
            check((rotten[0], rotten[1] + 1))
            check((rotten[0], rotten[1] - 1))
            if not cur:
                count += 1
                if self.remain == 0:
                    return count
                else:
                    if not next:
                        return -1
                    else:
                        cur = next
                        next = []

    def minKBitFlipsNK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        # Greedy即为最优？
        for i in range(0, len(A) - K + 1):
            if A[i] == 0:
                for j in range(i, i + K):
                    A[j] ^= 1
                res += 1
        for i in range(len(A)-K+1,len(A)):
            if A[i] == 0:
                return -1
        return res

    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        # 加速 i与i+1各自反转两次，替代K遍历,最终实际变化位置为i与i+K两个位置,其他位置不变
        memo = []
        for i in range(len(A) - K):
            if A[i] == 0:
                A[i] = 1
                A[i+K] ^= 1
                if len(memo) > 0 and memo[-1] == i:
                    #说明这一位不应该变化
                    memo.pop()
                else:
                    memo.append(i)
                memo.append(i+1)
        if sum(A[len(A) - K:]) == 0:
            if (len(A) - K) in memo:
                #同上
                memo.remove(len(A)-K)
            else:
                memo.append(len(A)-K)
        if sum(A[len(A) - K:]) == 0 or sum(A[len(A) - K:]) == K:
            return len(memo)
        else:
            return -1


    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 1: diff
        # 2: same
        # all nums must be used
        # all nums must sqrt(A[i] + A[i+1]) -> int
        dic = {}
        tarDic = {}
        for elem in A:
            if elem not in dic:
                dic[elem] = 1
            else:
                dic[elem] += 1
        elemList = list(dic.keys())
        for elem in elemList:
            tarDic[elem] = set()
        for i in elemList:
            for j in elemList:
                if i == j and dic[i] < 2:
                    continue
                cur = math.sqrt(i + j)
                if cur == 0 or cur % int(cur) == 0:
                    tarDic[i].add(j)
                    tarDic[j].add(i)
        # take even the same as an independent, but remeber to remove in that case
        final = 0
        N = len(A)

        # the dic is very small, manipulate and renew should be supported
        def search(cur, curDic, count):
            res = 0
            if count == N - 1:
                return 1
            for elem in tarDic[cur]:
                if curDic[elem] > 0:
                    newDic = dict(curDic)
                    newDic[elem] -= 1
                    res += search(elem, newDic, count + 1)
            return res

        for elem in elemList:
            curDic = dict(dic)
            curDic[elem] -= 1
            final += search(elem, curDic, 0)
        return final


A = Solution()

print(A.minKBitFlips([0,0,0,1,0,1,1,0],3))
