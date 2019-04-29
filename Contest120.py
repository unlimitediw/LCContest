class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        start = [-1, -1]
        curRemain = 0
        memoDic = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 0:
                    curRemain += 1

        def check(pos, pattern, remain):
            if 0 <= pos[0] < len(pattern) and 0 <= pos[1] < len(pattern[0]):
                if pattern[pos[0]][pos[1]] == 0:
                    newP = [p[:] for p in pattern]
                    newP[pos[0]][pos[1]] = -1
                    return search(pos,newP,remain - 1)
                elif pattern[pos[0]][pos[1]] == 2 and remain == 0:
                    return 1
            return 0

        def search(pos, pattern, remain):
            tupleP = tuple([tuple(pos)] + [tuple(p) for p in pattern])
            if tupleP not in memoDic:
                memoDic[tupleP] = 0
                memoDic[tupleP] += check([pos[0] + 1, pos[1]], pattern, remain)
                memoDic[tupleP] += check([pos[0] - 1, pos[1]], pattern, remain)
                memoDic[tupleP] += check([pos[0], pos[1] + 1], pattern, remain)
                memoDic[tupleP] += check([pos[0], pos[1] - 1], pattern, remain)
            return memoDic[tupleP]
        res = search(start,grid,curRemain)
        return res


A = Solution()
print(A.uniquePathsIII([[0,1],[2,0]]))
