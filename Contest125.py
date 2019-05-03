class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # suppose no duplicate

        notJudge = set()
        beTrust = {}
        for i in range(N):
            beTrust[i + 1] = 0
        for r in trust:
            if r[0] not in notJudge:
                notJudge.add(r[0])
            beTrust[r[1]] += 1
        find = False
        res = 0
        for p in beTrust.keys():
            if p not in notJudge:
                if beTrust[p] == N - 1:
                    if find:
                        return -1
                    else:
                        find = True
                        res = p
        if find:
            return res
        return -1

    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rook = [-1, -1]
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    rook = [i, j]
        # top
        for i in range(rook[0] - 1, -1, -1):
            if board[i][rook[1]] == 'p':
                res += 1
                break
            elif board[i][rook[1]] == 'B':
                break
        # down
        for i in range(rook[0] + 1, len(board)):
            if board[i][rook[1]] == 'p':
                res += 1
                break
            elif board[i][rook[1]] == 'B':
                break
        # left
        for i in range(rook[1] - 1, -1, -1):
            if board[rook[0]][i] == 'p':
                res += 1
                break
            elif board[rook[0]][i] == 'B':
                break
        # right
        for i in range(rook[1] + 1, len(board[0])):
            if board[rook[0]][i] == 'p':
                res += 1
                break
            elif board[rook[0]][i] == 'B':
                break
        return res

    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        # recover
        def recover(node):
            if not node:
                return []
            cur = [node.val]
            cur = recover(node.left) + cur
            cur = cur + recover(node.right)
            return cur

        cur = recover(root)
        cur.append(val)

        # build
        def build(valList):
            if not valList:
                return None
            maxIdx = 0
            for i in range(1, len(valList)):
                if valList[i] > valList[maxIdx]:
                    maxIdx = i
            node = TreeNode(valList[maxIdx])
            node.left = build(valList[:maxIdx])
            node.right = build(valList[maxIdx + 1:])
            return node

        res = build(cur)
        return res

    def gridIlluminationOld(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        board = [[0 for _ in range(N)] for _ in range(N)]

        def turnOn(pos):
            offset = pos[0] - pos[1]
            sumset = pos[0] + pos[1]
            for i in range(N):
                board[pos[0]][i] += 1
                board[i][pos[1]] += 1
                if 0 <= i + offset < N:
                    board[i + offset][i] += 1
                if 0 <= sumset - i < N:
                    board[i][sumset - i] += 1
            board[pos[0]][pos[1]] -= 3

        lampsSet = set()
        for lamp in lamps:
            lampsSet.add((lamp[0], lamp[1]))
            turnOn(lamp)

        def turnOff(pos):
            if 0 <= pos[0] < N and 0 <= pos[1] < N:
                if pos in lampsSet:
                    lampsSet.remove(pos)
                    offset = pos[0] - pos[1]
                    sumset = pos[0] + pos[1]
                    for i in range(N):
                        board[pos[0]][i] -= 1
                        board[i][pos[1]] -= 1
                        if 0 <= i + offset < N:
                            board[i + offset][i] -= 1
                        if 0 <= sumset - i < N:
                            board[i][sumset - i] -= 1
                    board[pos[0]][pos[1]] += 3

        def checkLight(pos):
            if board[pos[0]][pos[1]] > 0:
                res.append(1)
            else:
                res.append(0)
            turnOff((pos[0], pos[1]))
            turnOff((pos[0], pos[1] - 1))
            turnOff((pos[0], pos[1] + 1))
            turnOff((pos[0] - 1, pos[1]))
            turnOff((pos[0] - 1, pos[1] - 1))
            turnOff((pos[0] - 1, pos[1] + 1))
            turnOff((pos[0] + 1, pos[1]))
            turnOff((pos[0] + 1, pos[1] - 1))
            turnOff((pos[0] + 1, pos[1] + 1))

        for query in queries:
            checkLight(query)
        # 小N可以 想象一下大N分布的棋子，每次碰到就要改至多6 * 10^9次，不合理
        # 如果是database，应该记录的是行列而不是点！

        return res

    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        hori = {}
        verti = {}
        dia = {}
        anti_dia = {}

        def turnOn(pos):
            offset = pos[0] - pos[1]
            sumset = pos[0] + pos[1]
            if pos[0] not in hori:
                hori[pos[0]] = 1
            else:
                hori[pos[0]] += 1
            if pos[1] not in verti:
                verti[pos[1]] = 1
            else:
                verti[pos[1]] += 1
            if offset + N - 1 not in dia:
                dia[offset + N - 1] = 1
            else:
                dia[offset + N - 1] += 1
            if sumset not in anti_dia:
                anti_dia[sumset] = 1
            else:
                anti_dia[sumset] += 1

        lampsSet = set()
        for lamp in lamps:
            lampsSet.add((lamp[0], lamp[1]))
            turnOn(lamp)

        def turnOff(pos):
            if 0 <= pos[0] < N and 0 <= pos[1] < N:
                if pos in lampsSet:
                    lampsSet.remove(pos)
                    offset = pos[0] - pos[1]
                    sumset = pos[0] + pos[1]

                    hori[pos[0]] -= 1
                    verti[pos[1]] -= 1
                    dia[offset + N - 1] -= 1
                    anti_dia[sumset] -= 1

        def checkLight(pos):
            offset = pos[0] - pos[1]
            sumset = pos[0] + pos[1]
            if (pos[0] in hori and hori[pos[0]] > 0) or (pos[1] in verti and verti[pos[1]] > 0) or (offset + N - 1 in dia and dia[offset + N - 1] > 0) or (sumset in anti_dia and anti_dia[sumset] > 0):
                res.append(1)
            else:
                res.append(0)
            turnOff((pos[0], pos[1]))
            turnOff((pos[0], pos[1] - 1))
            turnOff((pos[0], pos[1] + 1))
            turnOff((pos[0] - 1, pos[1]))
            turnOff((pos[0] - 1, pos[1] - 1))
            turnOff((pos[0] - 1, pos[1] + 1))
            turnOff((pos[0] + 1, pos[1]))
            turnOff((pos[0] + 1, pos[1] - 1))
            turnOff((pos[0] + 1, pos[1] + 1))

        for query in queries:
            checkLight(query)
        # 小N可以 想象一下大N分布的棋子，每次碰到就要改至多6 * 10^9次，不合理
        # 如果是database，应该记录的是行列而不是点！
        # 这一次 memory error...
        return res


A = Solution()
