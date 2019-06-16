import collections


class Solution:
    def duplicateZeros(self, arr: list) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        next = []
        for i in range(len(arr)):
            next.append(arr[i])
            if arr[i] == 0:
                next.append(0)
            if len(next) >= len(arr):
                break
        arr[:] = next[:len(arr)]

    def largestValsFromLabels(self, values: list, labels: list, num_wanted: int, use_limit: int) -> int:
        memo = collections.defaultdict(int)
        total = []
        for i in range(len(values)):
            total.append((values[i], labels[i]))
        total = sorted(total)[::-1]
        res = []
        for i in range(len(total)):
            if memo[total[i][1]] < use_limit:
                res.append(total[i][0])
                memo[total[i][1]] += 1
            if len(res) == num_wanted:
                break
        return sum(res)

    def shortestPathBinaryMatrix(self, grid: list) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        N = len(grid)
        visited = {(0, 0)}
        memo = collections.defaultdict(list)
        memo[1] = [(0, 0)]
        self.found = False
        self.res = -1

        def check(pos):
            if 0 <= pos[0] < N and 0 <= pos[1] < N and grid[pos[0]][pos[1]] == 0:
                return True
            return False

        def visit(pos, length):
            if pos == (N - 1, N - 1):
                self.found = True
                self.res = length
            for next_pos in [(pos[0] - 1, pos[1] - 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1),
                             (pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]),
                             (pos[0] - 1, pos[1] + 1), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)]:
                if check(next_pos) and next_pos not in visited:
                    visited.add(next_pos)
                    memo[length + 1].append(next_pos)

        while memo.keys() and not self.found:
            cur_length = min(memo.keys())
            cur_pos_list = memo[cur_length]
            del memo[cur_length]
            for cur_pos in cur_pos_list:
                visit(cur_pos, cur_length)
                if self.found:
                    break
        return self.res

    def shortestCommonSupersequenceOld(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            temp = str1
            str1 = str2
            str2 = temp

        cur = str2 + str1

        def checksub(s1, s2):
            if len(s1) < len(s2):
                temp = s1
                s1 = s2
                s2 = temp
            j = 0
            for i in range(len(s2)):
                if j == len(s1):
                    return False
                while s2[i] != s1[j]:
                    j += 1
                    if j == len(s1):
                        return False
                j += 1
            return True

        for i in range(len(str1) + len(str2)):
            this = ''
            if i < len(str2):
                if checksub(str2[-i:], str2[:-i] + str1):
                    this = str2[:-i] + str1
                    while checksub()
            elif i <= len(str1):
                if checksub(str2, str1):
                    this = str1
            else:
                if checksub(str2[:len(str1) - i], str1 + str2[len(str1) - i:]):
                    this = str1 + str2[len(str1) - i:]
            if this and len(this) < len(cur):
                cur = this
        return cur

    # dp + LCS
    def shortestCommonSupersequence(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=lambda x: len(x))
        s = dp[m][n]

        i, j = 0, 0
        res = []
        for ch in s:
            newi = s1.find(ch, i)
            newj = s2.find(ch, j)

            res.append(s1[i:newi])
            res.append(s2[j:newj])
            res.append(ch)
            i, j = newi + 1, newj + 1

        res.append(s1[i:])
        res.append(s2[j:])
        return "".join(res)

A = Solution()
print(A.shortestCommonSupersequence("bcacaaab",
                                    "bbabaccc"))
print(A.shortestCommonSupersequence("abac",
                                    "acv"))
print(len('bbabacbcacaaab'))
