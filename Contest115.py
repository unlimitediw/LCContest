class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # all nodes as far as left in the last level
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        n = []
        status = 0
        while q:
            cur = q.pop(0)
            if status == 0:
                if not cur.left and not cur.right:
                    status = 1
                elif not cur.left:
                    return False
                elif not cur.right:
                    n.append(cur.left)
                    status = 1
                else:
                    n.append(cur.left)
                    n.append(cur.right)
            elif status == 1:
                if cur.left or cur.right:
                    return False
            if not q:
                q = n
                n = []
        return True

    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N == 0:
            return cells

        def check(pos, pre):
            if 0 <= pos < len(cells):
                return pre[pos]
            return -5

        c = 0
        pre = cells
        new = []
        memo = {}
        T = 0
        while c < N:
            for i in range(len(cells)):
                cur = check(i - 1, pre) + check(i + 1, pre)
                if cur == 0 or cur == 2:
                    new.append(1)
                else:
                    new.append(0)
            c += 1
            pre = new
            new = []
            cur = tuple(pre)
            if cur not in memo:
                memo[cur] = [c]
            elif len(memo[cur]) == 1:
                T = c - memo[cur][0]
                memo[cur] = [memo[cur][0], T]
            else:
                break
        if c == N:
            return pre
        remain = N % T
        if remain == 0:
            remain = T
        for key, val in memo.items():
            if val[0] == remain:
                return list(key)

    # DFS rather pattern search. the key point is each point. should not care about the pattern
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        newGrid = []
        for s in grid:
            cur = []
            for i in range(len(s)):
                if s[i] == '/':
                    cur.append(1)
                elif s[i] == " ":
                    cur.append(3)
                else:
                    cur.append(2)
            newGrid.append(cur)
            print(cur)
        grid = newGrid
        m = len(grid)
        n = len(grid[0])

        count = 0
        pre = [1 for _ in range(2 * n)]
        next = [1] + [0 for _ in range(2 * n - 2)] + [1]
        for i in range(2 * m):
            curI = i // 2
            next = [1] + [0 for _ in range(2 * n - 2)] + [1]
            for j in range(2 * n):
                curJ = j // 2
                if grid[curI][curJ] == 1 and j % 2 == 1:
                    if pre[j] == 1:
                        next[j - 1] = 1
                        if j - 1 > 0:
                            next[j - 2] = 1
                if grid[curI][curJ] == 2 and j % 2 == 0:
                    if pre[j] == 1:
                        next[j + 1] = 1
                        if j + 1 < 2 * n - 1:
                            next[j + 2] = 1
            i += 1
            # iter 1
            pre = next
            if i == 2 * m - 1:
                next = [1 for _ in range(2 * n)]
            else:
                next = [1] + [0 for _ in range(2 * n - 2)] + [1]
            for j in range(2 * n):
                curJ = j // 2
                if grid[curI][curJ] == 1 and j % 2 == 0:
                    if pre[j + 1] == 1:
                        print(i,j)
                        if next[j] == 1:
                            count += 1
                        else:
                            next[j] = 1
                            if j > 0:
                                next[j - 1] = 1
                        print("**")
                if grid[curI][curJ] == 2 and j % 2 == 1:
                    if pre[j - 1] == 1:
                        if next[j] == 1:
                            count += 1
                        else:
                            next[j] = 1
                            if j < 2 * n - 1:
                                next[j + 1] = 1
            pre = next

            print(pre)
            print(next)
            print("*****")
        return count
            # iter 2


A = Solution()
print(A.regionsBySlashes([
    "//",
    "/ "
]))
