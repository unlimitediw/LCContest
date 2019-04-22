class Solution:
    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':
        def translate(text):
            res = ''
            for c in text:
                if c == '#':
                    res = res[:-1]
                else:
                    res += c
            return res
        return translate(S) == translate(T)

    def longestMountain(self, A: 'List[int]') -> 'int':
        res = 0
        if len(A) < 3:
            return res
        up = 0
        down = 0
        status = 0 # 0 mean flatten, 1 up, 2 down
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                if status == 1:
                    up += 1
                elif status == 2:
                    if up != 0:
                        res = max(res,up+down)
                    status = 1
                    up = 1
                    down = 0
                else:
                    status = 1
                    up = 1
            elif A[i] < A[i-1]:
                if status == 1:
                    down += 1
                    status = 2
                elif status == 2:
                    down += 1
            else:
                if up != 0 and down != 0:
                    res = max(res, up + down)
                up = 0
                down = 0
                status = 0
        if up != 0 and down != 0:
            res = max(res, up + down)
        if res == 0:
            return 0
        else:
            return res + 1

    def isNStraightHand(self, hand: 'List[int]', W: 'int') -> 'bool':
        hand.sort()
        memoDic = {}
        for elem in hand:
            if elem not in memoDic:
                memoDic[elem] = 1
            else:
                memoDic[elem] += 1
        checkList = list(memoDic.keys())
        count = 0
        while True:
            cur = checkList[:W]
            if len(cur) != W:
                return False
            for i in range(len(cur)):
                if i > 0:
                    if cur[i] - cur[i-1] != 1:
                        return False
                memoDic[cur[i]] -= 1
                if memoDic[cur[i]] == 0:
                    if cur[i] != checkList[0]:
                        return False
                    checkList.pop(0)
                elif memoDic[cur[i]] < 0:
                    return False
            count += W
            if count == len(hand):
                return True

    def shortestPathLength(self, graph):
        # BFS solution
        # 32 刚好是每种路径都走一次
        memo, final, q, steps = set(), (1 << len(graph)) - 1, [(i, 1 << i) for i in range(len(graph))], 0
        print(q)
        while True:
            new = []
            for node, state in q:
                if state == final: return steps
                for v in graph[node]:
                    if (v,state | 1 << v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((v, state | 1 << v))
            q = new
            steps += 1

'''
Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
'''

A = Solution()

print(A.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))