class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        A = [a, b, c]
        A = sorted(A)
        x = A[0]
        y = A[1]
        z = A[2]
        minV = (min(1, y - x - 1) + min(1, z - y - 1))
        if y - x > 1:
            minV = min(minV, y - x - 1)
        if z - y > 1:
            minV = min(minV, z - y - 1)
        maxV = z - x - 2
        return [minV, maxV]

    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        cur = grid[r0][c0]
        visited = set()
        newG = []
        for g in grid:
            newG.append(g[:])

        def check(pos):
            if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                if grid[pos[0]][pos[1]] != cur:
                    return True
            return False

        def visit(pos):
            visited.add(pos)
            if pos[0] == 0 or pos[0] == len(grid) - 1 or pos[1] == 0 or pos[1] == len(grid[0]) - 1 or check(
                    [pos[0] + 1, pos[1]]) or check([pos[0] - 1, pos[1]]) or check([pos[0], pos[1] + 1]) or check(
                [pos[0], pos[1] - 1]):
                newG[pos[0]][pos[1]] = color
            if pos[0] + 1 < len(grid) and grid[pos[0] + 1][pos[1]] == cur and (pos[0] + 1, pos[1]) not in visited:
                visit((pos[0] + 1, pos[1]))
            if 0 <= pos[0] - 1 and grid[pos[0] - 1][pos[1]] == cur and (pos[0] - 1, pos[1]) not in visited:
                visit((pos[0] - 1, pos[1]))
            if pos[1] + 1 < len(grid[0]) and grid[pos[0]][pos[1] + 1] == cur and (pos[0], pos[1] + 1) not in visited:
                visit((pos[0], pos[1] + 1))
            if 0 <= pos[1] - 1 and grid[pos[0]][pos[1] - 1] == cur and (pos[0], pos[1] - 1) not in visited:
                visit((pos[0], pos[1] - 1))

        visit((r0, c0))
        return newG

    def maxUncrossedLinesOld(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        digitA = {}
        digitB = {}
        for i in range(len(A)):
            if A[i] not in digitA:
                digitA[A[i]] = [i]
            else:
                digitA[A[i]].append(i)
        for i in range(len(B)):
            if B[i] not in digitB:
                digitB[B[i]] = [i]
            else:
                digitB[B[i]].append(i)
        lineSet = []
        for key in digitA.keys():
            for i in digitA[key]:
                if key in digitB:
                    for j in digitB[key]:
                        lineSet.append((i, j))
        lineSet.sort()
        if not lineSet:
            return 0

        '''
        # Old version
        curMax = 1
        stack = [lineSet[0]]
        for i in range(1,len(lineSet)):
        if lineSet[i][0] == stack[-1][0]:
            continue
        while lineSet[i][1] <= stack[-1][1]:
            if i + 1 < len(lineSet) and lineSet[i+1][0] == lineSet[i][0]:
                i += 1
                continue
            stack.pop()
            if not stack:
                break
        stack.append(lineSet[i])
        curMax = max(curMax,len(stack))
        '''

        '''
        # version2
        resList = [[lineSet[0],1]]
        for i in range(1,len(lineSet)):
            newRes = []
            cur = [0,0]
            for res in resList:
                if res[0][0] < lineSet[i][0] and res[0][1] < lineSet[i][1]:
                    if res[1] + 1 > cur[1]:
                        cur[0] = lineSet[i]
                        cur[1] = res[1] + 1
                else:
                    newRes.append(res)
            if not cur[0]:
                newRes.append([lineSet[i], 1])
            else:
                newRes.append(cur)
            resList = newRes
        curMax = 1
        print(resList)
        for res in resList:
            curMax = max(curMax,res[1])
        return curMax

        '''

        '''
        # version 3
        resList = [[0]]
        visited = set()
        for i in range(1,len(lineSet)):
            newRes = []
            for res in resList:
                if lineSet[res[-1]][0] < lineSet[i][0] and lineSet[res[-1]][1] < lineSet[i][1]:
                    res.append(i)
                    newRes.append(res)
                else:
                    newRes.append(res[:])
                    while res and (lineSet[res[-1]][0] >= lineSet[i][0] or lineSet[res[-1]][1] >= lineSet[i][1]):
                        res.pop()
                    res.append(i)
                    #print(res)
                    cur = tuple(res)
                    if cur not in visited:
                        visited.add(cur)
                        newRes.append(res)
            resList = newRes
        curMax = 1
        for res in resList:
            print(res)
        for res in resList:
            curMax = max(curMax,len(res))
        return curMax
        '''

    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # construct DP and lines
        dp = [[0 for _ in range(len(B))] for _ in range(len(A))]
        lines = [[0 for _ in range(len(B))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    lines[i][j] = 1
        # Construct Dp
        dp[0][0] = lines[0][0]
        ia = 0
        ib = 0

        for i in range(1, len(A)):
            dp[i][0] = max(lines[i][0], dp[i - 1][0])
        for i in range(1, len(B)):
            dp[0][i] = max(lines[0][i], dp[0][i - 1])
        while ia != len(A) - 1 or ib != len(B) - 1:
            if ia != len(A) - 1:
                ia += 1
                for i in range(1, len(B)):
                    dp[ia][i] = max(dp[ia - 1][i - 1] + lines[ia][i], dp[ia - 1][i], dp[ia][i - 1])
            if ib != len(B) - 1:
                ib += 1
                for i in range(1, len(A)):
                    dp[i][ib] = max(dp[i - 1][ib - 1] + lines[i][ib], dp[i][ib - 1], dp[i - 1][ib])
            if ia > 0 and ib > 0:
                dp[ia][ib] = max([dp[ia - 1][ib - 1] + lines[ia][ib], dp[ia - 1][ib], dp[ia][ib - 1]])
            elif ia > 0:
                dp[ia][ib] = dp[ia - 1][ib]
            elif ib > 0:
                dp[ia][ib] = dp[ia][ib - 1]
        return dp[-1][-1]

    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """

        # enclosed
        '''
        # * # *
        * * * *
        * * # #
        * # * *
        '''
        # only 200 blocked, so find the blocked area by it
        blockSet = set()
        for block in blocked:
            blockSet.add(tuple(block))

        # 对所有enclosed同false同true，则return true

        # 进一步想象，blocked size 200,那么所围面积必然小于200，如果200次内都没搜到目标且没有多余空间可搜，则为无解

        visited = {(source[0], source[1])}
        target = (target[0], target[1])
        queue = [(source[0], source[1])]

        def check(pos):
            if pos not in visited and 0 <= pos[0] < 10 ** 6 and 0 <= pos[1] < 10 ** 6 and pos not in blockSet:
                visited.add(pos)
                return True
            return False
        N = (len(blocked) * len(blocked))//2 + 1
        count = 0
        while queue:
            count += 1
            cur = queue.pop(0)
            if check((cur[0] + 1, cur[1])):
                if (cur[0] + 1, cur[1]) == target: return True
                queue.append((cur[0] + 1, cur[1]))
            if check((cur[0] - 1, cur[1])):
                if (cur[0] - 1, cur[1]) == target: return True
                queue.append((cur[0] - 1, cur[1]))
            if check((cur[0], cur[1] + 1)):
                if (cur[0], cur[1] + 1) == target: return True
                queue.append((cur[0], cur[1] + 1))
            if check((cur[0], cur[1] - 1)):
                if (cur[0], cur[1] - 1) == target: return True
                queue.append((cur[0], cur[1] - 1))
            if count > N:
                break
        if count <= N:
            return False
        return True


A = Solution()
a = [1, 1, 1, 1, 3, 3]
b = [1, 1, 3, 2, 2, 3]
print(A.isEscapePossible([],[0,0],[999999,999999]))
