import bisect
from collections import defaultdict


class Solution:
    def toGoatLatin(self, S: str) -> str:
        str_list = S.split(' ')
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = ''
        for i, cur in enumerate(str_list):
            if cur[0] in vowel:
                res += cur
            else:
                res += cur[1:] + cur[0]
            res += 'ma'
            res += 'a' * (i + 1)
            res += ' '
        res = res[:len(res) - 1]
        return res

    def numFriendRequests(self, ages: list) -> int:
        res = 0
        ages.sort()
        tail_dic = {}
        for i in range(len(ages)):
            tail_dic[ages[i]] = i
        i = 0
        while i < len(ages):
            j = tail_dic[ages[i]]
            res += (j - i + 1) * (j - bisect.bisect_right(ages[:j], ages[j] * 0.5 + 7))
            i = j
            i += 1
        return res

    def maxProfitAssignment(self, difficulty: list, profit: list, worker: list) -> int:
        worker.sort()
        memo = defaultdict(int)
        for i in range(len(difficulty)):
            memo[difficulty[i]] = max(memo[difficulty[i]], profit[i])
        difficulty = list(set(difficulty))
        difficulty.sort()
        new_diff = []
        pre = 0
        for diff in difficulty:
            if memo[diff] > pre:
                new_diff.append(diff)
                pre = memo[diff]
        res = 0
        for work in worker:
            i = bisect.bisect_right(new_diff, work) - 1
            if i >= 0:
                res += memo[new_diff[i]]
        return res

    def largestIsland(self, grid: list) -> int:
        visited = set()
        cur_island = 0
        space_memo = {}
        island_memo = {}

        def search(pos, cur):
            i, j = pos[0], pos[1]
            if pos not in visited and 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                visited.add(pos)
                if grid[i][j] == 1:
                    island_memo[(i, j)] = cur
                    space_memo[cur] += 1
                    search((i + 1, j), cur)
                    search((i - 1, j), cur)
                    search((i, j + 1), cur)
                    search((i, j - 1), cur)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    cur_island += 1
                    space_memo[cur_island] = 0
                    search((i, j), cur_island)
        res = max(list(space_memo.values()) + [0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    cur_val = 0
                    cur_set = set()
                    visit_list = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                    for visit in visit_list:
                        if visit in island_memo:
                            cur_set.add(island_memo[visit])
                    for cur in cur_set:
                        cur_val += space_memo[cur]
                    res = max(cur_val + 1, res)
        return res


A = Solution()
print(A.largestIsland([[0, 0], [0, 0]]))
