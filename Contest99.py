class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        Count = 0
        total = 0
        n, m = len(grid),len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    Count += 2
                    total += grid[i][j]
        def checkBound(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                return 0
            return 1
        while total:
            memo = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
            for i in range(n):
                for j in range(m):
                    if grid[i][j]:
                        Count += checkBound(i+1,j)
                        Count += checkBound(i,j+1)
                        Count += checkBound(i-1,j)
                        Count += checkBound(i,j-1)
                        memo[i][j] += 1
                        total -= 1
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    grid[i][j] -= memo[i][j]
        return Count

    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        B = set()
        for string in A:
            C = list(string)
            a, b = C[::2], C[1::2]
            B.add((''.join(sorted(a)), ''.join(sorted(b))))

        return len(B)

    def allPossibleFBTOld(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        def selfiter(remain):
            if remain == 0:
                return [TreeNode(0)]
            nodeList = []
            if N >= 4:
                child1 = selfiter(remain - 4)
                child2 = selfiter(remain - 4)
                for i in range(len(child1)):
                    cur = TreeNode(0)
                    cur.left = child1[i]
                    cur.right = child2[i]
                    nodeList.append(cur)
            if N >= 2:
                for subNode in selfiter(remain - 2):
                    cur = TreeNode(0)
                    cur.left = subNode
                    nodeList.append(cur)
                    cur = TreeNode(0)
                    cur.right = subNode
                    nodeList.append(cur)
            return nodeList
        return selfiter(N)

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        def selfIter(remain):
            if remain == 0:
                return [TreeNode(0)]
            localRes = []
            for i in range(2,remain+1,2):
                j = remain - i + 2
                leftSet = selfIter(remain - i)
                rightSet = selfIter(remain - j)
                for left in leftSet:
                    for right in rightSet:
                        new = TreeNode(0)
                        new.left = left
                        new.right = right
                        localRes.append(new)
            return localRes
        res = []
        for i in range(2, N + 1, 2):
            j = N - i + 2
            leftSet = selfIter(N - i + 1)
            rightSet = selfIter(N - j + 1)
            for left in leftSet:
                for right in rightSet:
                    new = TreeNode(0)
                    new.left = left
                    new.right = right
                    res.append(new)
        return res

class FreqStack(object):

    def __init__(self):
        self.freqDic = {}
        self.stack = []
        pass

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x not in self.freqDic:
            self.freqDic[x] = 1
        else:
            self.freqDic[x] += 1

    def pop(self):
        """
        :rtype: int
        """
        keySet = []
        for key in self.freqDic:
            if not keySet:
                keySet = [key]
            if self.freqDic[key] > self.freqDic[keySet[0]]:
                keySet = [key]
            elif self.freqDic[key] == self.freqDic[keySet[0]]:
                keySet.append(key)
        keySet = set(keySet)
        cur = -1
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] in keySet:
                cur = i
                break
        self.freqDic[self.stack[i]] -= 1
        return self.stack.pop(i)


print(len([[0,0,0,0,0,None,None,0,0],[0,0,0,0,0,None,None,None,None,0,0],[0,0,0,0,0,0,0],[0,0,0,None,None,0,0,0,0],[0,0,0,None,None,0,0,None,None,0,0]]))
print(Solution().surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))