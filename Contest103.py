class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        A_max = max(A)
        A_min = min(A)
        return max(A_max - A_min - 2 * K, 0)

    # can not check pre
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        height = len(board)
        width = len(board[0])
        totalLength = height * width
        mapHistory = {}
        for i in range(totalLength):
            count = 1
            while count < 7 and i - count >= 0:
                if i not in mapHistory:
                    mapHistory[i] = [i - count]
                else:
                    mapHistory[i].append(i - count)
                count += 1

        if totalLength == 0:
            return 0

        # dp from end to start, calculate the steps for each
        dp = [0 for _ in range(height * width)]
        dpQueue = []
        for i in range(totalLength):
            dpQueue.append(i)
        visited = set()

        while dpQueue:
            break
            cur = dpQueue.pop(0)
            print(cur)
            if cur == 0:
                dp[cur] = 0
            else:
                row = cur % width
                if row % 2 == 1:
                    col = (width - 1 - i % width)
                else:
                    col = i % width
                if board[row][col] != -1:
                    if totalLength - board[row][col] not in visited:
                        mapHistory[totalLength - board[row][col]].remove(cur)
                        dpQueue.append(cur)
                    else:
                        dp[i] = dp[totalLength - board[row][col]]
                        visited.add(cur)
                else:
                    can = True
                    for pre in mapHistory[cur]:
                        if pre not in visited:
                            dpQueue.append(cur)
                            can = False
                            break
                    if can:
                        visited.add(cur)
                        min = dp[cur - 1]
                        for pre in mapHistory[cur]:
                            min = dp[pre] if dp[pre] < min else min
                        dp[cur] = min + 1
        return dp[totalLength - 1]

    def snakesAndLadders2(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        height = len(board)
        width = len(board[0])


check = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]]
A = Solution()
print(A.snakesAndLadders(check))

a = {3:[4,5]}
a[3].remove(4)
print(a)
