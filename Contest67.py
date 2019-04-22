class Solution:
    def countPrimeSetBits(self, L: 'int', R: 'int') -> 'int':
        res = 0

        def checkPrime(num):
            if num == 0 or num == 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def numOfOne(num):
            cur = bin(num)
            count = 0
            for c in cur:
                if c == '1':
                    count += 1
            return count

        for val in range(L, R + 1):
            if checkPrime(numOfOne(val)):
                res += 1
        return res

    def partitionLabels(self, S: 'str') -> 'List[int]':
        eDic = {}
        res = []
        start = 0
        for i in range(len(S)):
            eDic[S[i]] = i
        curE = eDic[S[0]]
        for i in range(len(S)):
            if i < curE:
                curE = max(eDic[S[i]], curE)
            else:
                res.append(i - start + 1)
                start = i + 1
                if i + 1 < len(S):
                    curE = eDic[S[i + 1]]
        return res

    def orderOfLargestPlusSign(self, N: 'int', mines: 'List[List[int]]') -> 'int':
        board = [[[N, N] for _ in range(N)] for _ in range(N)]
        for mine in mines:
            board[mine[0]][mine[1]] = -1
        for i in range(N):
            for j in range(N):
                if board[i][j] != -1:
                    board[i][j][0] = min(i, N - i - 1)
                    board[i][j][1] = min(j, N - j - 1)
        for i in range(N):
            start = False
            for j in range(N):
                if board[i][j] == -1:
                    if not start:
                        start = True
                        for q in range(0, j):
                            board[i][q][1] = min(j - q - 1, board[i][q][1])
                    findBound = False
                    for k in range(j + 1, N):
                        if board[i][k] == -1:
                            findBound = True
                            for q in range(j + 1, k):
                                board[i][q][1] = min(q - j - 1, board[i][q][1], k - q - 1)
                            j = k
                            break
                    if not findBound:
                        for q in range(j + 1, N):
                            board[i][q][1] = min(N - j - 1, board[i][q][1], q - j - 1)
        for i in range(N):
            start = False
            for j in range(N):
                if board[j][i] == -1:
                    if not start:
                        start = True
                        for q in range(0, j):
                            board[q][i][0] = min(j - q - 1, board[q][i][0])
                    findBound = False
                    for k in range(j + 1, N):
                        if board[k][i] == -1:
                            findBound = True
                            for q in range(j + 1, k):
                                board[q][i][0] = min(q - j - 1, board[q][i][0], k - q - 1)
                            j = k
                            break
                    if not findBound:
                        for q in range(j + 1, N):
                            board[q][i][0] = min(N - j - 1, board[q][i][0], q - j - 1)
        res = 0

        for i in range(N):
            for j in range(N):
                if board[i][j] != -1:
                    res = max(res, min(board[i][j][0], board[i][j][1]) + 1)
        return res

    def minSwapsCouples(self, row: 'List[int]') -> 'int':
        # 找出异常配对
        # 如何让异常配对最快恢复？
        # 大-》小 小-》大 两种情况均可，如果只有一种情况，那一直更换错误项就一定是正确的，因为每个数字的位置是固定的
        # 但是在两种情况下，正确的组我们是不用动的，对于错误的组，有正反两种选择，要找出选择最快的那种
        # 首先构造一个两两配对寻址字典，每次操作都更新字典
        # 然后对两种操作进行bfs？2**60是极限， 这个是算不了的，那么试试用astar来做吧，异常组量就是heuristic

        # 2是不会对1的
        # 说明了一个问题，只要在一起就行
        # 比如说 3 7 1 2 6 5 4 9 8 0
        # 可以是 3 2 1 7 6 5 4 9 8 0

        # 或是   1 7 3 2 换7和2 和1换3 和 1没有任何区别
        # 但是 3 2 是问题所在 是肯定要换的
        # 所以见到异常就换就行了

        # 但是还有一种情况
        # 如果线换1 和8
        # 变成 3 7 8 2 6 5 4 9 1 0
        # 然后换3 和 8 两步变成 8 7 3 2 6 5 4 9 1 0
        # 如果是原来那样 还是一样的速度

        # queue里的元素
        # 应该包含已走步数 int
        # 数组的外貌 list
        # 异常的坐标 set
        # 对应坐标字典 dic
        count = 0
        memo = {}
        for i in range(len(row)):
            memo[row[i]] = i
        errorQ = []
        for i in range(0, len(row), 2):
            if abs(row[i + 1] - row[i]) != 1:
                errorQ.append(i)
        while errorQ:
            i = errorQ.pop()
            count += 1
            if row[i] % 2 == 0:
                temp = row[i + 1]
                row[i + 1] = row[i] + 1
                row[memo[row[i + 1]]] = temp
                memo[temp] = memo[row[i + 1]]
                memo[row[i + 1]] = i + 1
                next = memo[temp]
                if next % 2 == 0:
                    if ((row[next] - row[next + 1] == 1 and row[next] % 2 == 1) or (
                            row[next + 1] - row[next] == 1 and row[next] % 2 == 0)):
                        if next in errorQ:
                            errorQ.remove(next)
                    else:
                        if next not in errorQ:
                            errorQ.append(next)
                else:
                    if ((row[next] - row[next - 1] == 1 and row[next] % 2 == 1) or (
                            row[next - 1] - row[next] == 1 and row[next] % 2 == 0)):
                        if next - 1 in errorQ:
                            errorQ.remove(next - 1)
                    else:
                        if next - 1 not in errorQ:
                            errorQ.append(next - 1)
            else:
                temp = row[i + 1]
                row[i + 1] = row[i] - 1
                row[memo[row[i + 1]]] = temp
                memo[temp] = memo[row[i + 1]]
                memo[row[i + 1]] = i + 1
                next = memo[temp]
                if next % 2 == 0:
                    if ((row[next] - row[next + 1] == 1 and row[next] % 2 == 1) or (
                            row[next + 1] - row[next] == 1 and row[next] % 2 == 0)):
                        if next in errorQ:
                            errorQ.remove(next)
                    else:
                        if next not in errorQ:
                            errorQ.append(next)
                else:
                    if ((row[next] - row[next - 1] == 1 and row[next] % 2 == 1) or (
                            row[next - 1] - row[next] == 1 and row[next] % 2 == 0)):
                        if next - 1 in errorQ:
                            errorQ.remove(next - 1)
                    else:
                        if next - 1 not in errorQ:
                            errorQ.append(next - 1)
        return count


A = Solution()

print(A.minSwapsCouples([5,3,4,2,1,0]))
