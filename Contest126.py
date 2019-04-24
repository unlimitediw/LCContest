class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        memo = [float('inf') for _ in range(26)]
        for char in A[0]:
            memo[ord(char) - 97] += 1
        for a in A:
            newMemo = [0 for _ in range(26)]
            for char in a:
                newMemo[ord(char) - 97] += 1
            for i in range(26):
                memo[i] = min(memo[i], newMemo[i])
        res = []
        for i in range(26):
            while memo[i] > 0:
                memo[i] -= 1
                res.append(chr(97 + i))
        return res

    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        # S 是否可以游'abc'拆解插入'abc'得来
        cur = S
        i = 0
        while cur:
            res = ''
            findABC = False
            while i < len(cur):
                if cur[i:i + 3] == 'abc':
                    findABC = True
                    i += 3
                else:
                    res += cur[i]
                    i += 1
            cur = res
            i = 0
            if not findABC:
                return False
        return True

    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        if K == 0:
            One = False
            last = 0
            for i in range(len(A)):
                if A[i] == 1:
                    if not One:
                        One = True
                        last = i
                else:
                    if One:
                        res = max(res, i - last)
                        One = False
            if One:
                res = max(res, len(A) - last)
            return res
        else:
            sepPos = []
            meetOne = False
            lastOne = 0
            for i in range(len(A)):
                if A[i] == 0:
                    if K > 0:
                        if meetOne:
                            sepPos.append(lastOne)
                            meetOne = False
                        else:
                            sepPos.append(i)
                        if len(sepPos) > K:
                            pre = sepPos.pop(0)
                            res = max(res, i - pre)
                else:
                    if not meetOne:
                        lastOne = i
                        meetOne = True
            if not sepPos: return len(A)
            res = max(res, len(A) - sepPos[0])
            return res


    # learn from kernel, redo later
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        if not stones:
            if K == 0: return 0
            return -1
        N = len(stones)
        if (N - 1) % (K - 1) != 0: return -1

        cums = [0]
        for x in stones:
            cums.append(x + cums[-1])
        print(cums)
        dp = [[-10000] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 0

        for l in range(2, N + 1):
            for i in range(0, N - l + 1):
                j = i + l - 1
                dp[i][j] = min([dp[i][m] + dp[m + 1][j] for m in range(i, j, K - 1)])
                if (j - i) % (K - 1) == 0:
                    dp[i][j] += cums[j + 1] - cums[i]

        return dp[0][N - 1]


A = Solution()
print(A.mergeStones([3,5,1,2,6],3))

