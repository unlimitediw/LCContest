class Solution:
    def validMountainArray(self, A: list) -> bool:
        if len(A) < 3:
            return False
        up = True
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                return False
            if up:
                if A[i] < A[i - 1]:
                    if i == 1:
                        return False
                    up = False
            else:
                if A[i] > A[i - 1]:
                    return False
        if up:
            return False
        return True

    def minDeletionSize(self, A: list) -> int:
        if len(A) == 1:
            return 0
        res = 0
        for i in range(len(A[0])):
            for j in range(1, len(A)):
                if A[j][i] < A[j - 1][i]:
                    res += 1
                    break
        return res

    def diStringMatch(self, S: str) -> list:
        res = [0 for _ in range(len(S) + 1)]
        curI = 0
        curD = len(S)
        for i in range(len(S)):
            if S[i] == 'I':
                res[i] = curI
                curI += 1
                if i == len(S) - 1:
                    res[i + 1] = curI
            else:
                res[i] = curD
                curD -= 1
                if i == len(S) - 1:
                    res[i + 1] = curD
        return res

    def shortestSuperstringSlow(self, A: list) -> str:
        # set_size: left * right * length = 12 * 12 * (2**10)
        visited = {}
        self.res = ''
        n = len(A)
        memo = [[0 for _ in range(n)] for _ in range(n)]
        for i, word1 in enumerate(A):
            for j, word2 in enumerate(A):
                if i != j:
                    for k in range(min(len(word1), len(word2)))[::-1]:
                        if word1[-k:] == word2[:k]:
                            memo[i][j] = k
                            break

        def search(pre, l_idx, r_idx, step, cur):
            if (pre, l_idx, r_idx) in visited:
                if len(cur) >= visited[(pre, l_idx, r_idx)]:
                    return
            visited[(pre, l_idx, r_idx)] = len(cur)
            if step == len(A) - 1:
                # print(cur,len(cur))
                if not self.res:
                    self.res = cur
                elif len(cur) < len(self.res):
                    self.res = cur
            for i in range(len(A)):
                if not 2 ** i & pre:
                    new = pre | 2 ** i
                    left_merge_point = memo[i][l_idx]
                    right_merge_point = memo[r_idx][i]
                    left_merge = A[i] + cur[left_merge_point:]
                    right_merge = cur + A[i][right_merge_point:]
                    #print(left_merge,right_merge)
                    search(new, i, r_idx, step + 1, left_merge)
                    search(new, l_idx, i, step + 1, right_merge)

        search(1, 0, 0, 0, A[0])
        return self.res

    def shortestSuperstring(self, A: list) -> str:

        n = len(A)
        memo = [[0 for _ in range(n)] for _ in range(n)]
        for i, word1 in enumerate(A):
            for j, word2 in enumerate(A):
                if i != j:
                    for k in range(min(len(word1), len(word2)))[::-1]:
                        if word1[-k:] == word2[:k]:
                            memo[i][j] = k
                            break
        check = {}

        def search(pre, r_idx):
            if (pre, r_idx) in check:
                return check[(pre, r_idx)]
            if not (1 << r_idx) & pre:
                return ''
            if pre == (1 << r_idx):
                return A[r_idx]
            check[(pre, r_idx)] = ''
            for i in range(n):
                if i != r_idx and (1 << i) & pre:
                    cur = search(pre ^ (1 << r_idx), i) + A[r_idx][memo[i][r_idx]:]
                    if check[(pre, r_idx)] == '' or len(cur) < len(check[(pre, r_idx)]):
                        check[(pre, r_idx)] = cur
            return check[(pre, r_idx)]

        res = ''
        for k in range(n):
            cur = search((1 << n) - 1, k)
            if not res or len(cur) < len(res):
                res = cur
        return res


# should use bfs
# 12 * 11 种头部组合 * 2 ** 11种内部组合
# 先写出 12*12*2的对应插入长度表
# 然后 依次 12 * 11 * min (10)
# 10 * 9 * i
A = Solution()
print(A.shortestSuperstringSlow(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))
# print(len('ttcagctaagtcatgcatc'), len("gctaagttcatgcatc"))

# print(1<<2)
