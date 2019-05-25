from collections import defaultdict


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list:
        memo = defaultdict(int)
        for word in A.split():
            memo[word] += 1
        for word in B.split():
            memo[word] += 1
        res = []
        for key, val in memo.items():
            if val == 1:
                res.append(key)
        return res

    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> list:
        self.total = R * C

        self.step = 1
        self.count_step = 0
        self.memo = 0
        self.dir = 1  # 1 east 2 s 3 w 4 n
        cur = [r0, c0]
        res = []

        def visit(pos):

            if 0 <= pos[0] < R and 0 <= pos[1] < C:
                res.append(pos)
                self.total -= 1
            if self.dir == 1:

                next = [pos[0], pos[1] + 1]
            elif self.dir == 2:
                next = [pos[0] + 1, pos[1]]
            elif self.dir == 3:
                next = [pos[0], pos[1] - 1]
            else:
                next = [pos[0] - 1, pos[1]]
            self.count_step += 1
            if self.count_step == self.step:
                self.count_step = 0
                self.memo += 1
                self.dir = self.dir % 4 + 1
                if self.memo == 2:
                    self.memo = 0
                    self.step += 1
            return next

        while self.total > 0:
            cur = visit(cur)

        return res

    def possibleBipartition(self, N: int, dislikes: list) -> bool:

        visited = set()
        memo_one = set()
        memo_two = set()
        memo_pos = defaultdict(list)
        for i, dislike in enumerate(dislikes):
            memo_pos[dislike[0]].append((i,1))
            memo_pos[dislike[1]].append((i,0))

        for val in range(1, N + 1):
            if val not in visited:
                visited.add(val)
                A_queue = {val}
                B_queue = set()
                searchA = True
                while A_queue or B_queue:
                    if searchA:
                        cur = A_queue.pop()
                        visited.add(cur)
                        memo_one.add(cur)
                        for B_pos in memo_pos[cur]:
                            if dislikes[B_pos[0]][B_pos[1]] in memo_one:
                                print(1)
                                return False
                            if dislikes[B_pos[0]][B_pos[1]] not in visited:
                                B_queue.add(dislikes[B_pos[0]][B_pos[1]])
                        if not A_queue:
                            A_queue = set()
                            searchA = False
                    else:
                        cur = B_queue.pop()
                        visited.add(cur)
                        memo_two.add(cur)
                        for A_pos in memo_pos[cur]:
                            if dislikes[A_pos[0]][A_pos[1]] in memo_two:
                                return False
                            if dislikes[A_pos[0]][A_pos[1]] not in visited:
                                A_queue.add(dislikes[A_pos[0]][A_pos[1]])
                        if not B_queue:
                            B_queue = set()
                            searchA = True
        return True

    def superEggDrop(self, K, N):
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
print(A.possibleBipartition(5, [[1,2],[3,4],[4,5],[3,5]]))
