class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key not in self.dic:
            self.dic[key] = {}
            self.dic[key] = [[value,timestamp]]
        else:
            self.dic[key].append([value,timestamp])

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key in self.dic:
            compare = self.dic[key]
            for c in reversed(compare):
                if c[1] <= timestamp:
                    return c[0]
            return ''
        else:
            return ''


import math
class Solution:
    def strWithout3a3b(self, A: 'int', B: 'int') -> 'str':
        inverse = False
        if A < B:
            inverse = True
            temp = A
            A = B
            B = temp
        res = ''
        while True:
            if B == 0:
                for i in range(A):
                    res += 'a'
                break
            elif A > B:
                res += 'aab'
                A -= 2
                B -= 1
            elif A == B:
                res += 'ab'
                A -= 1
                B -= 1
        if inverse:
            res = list(res)
            for i in range(len(res)):
                if res[i] == 'a':
                    res[i] = 'b'
                else:
                    res[i] = 'a'
            newRes = ''
            for elem in res:
                newRes += elem
            res = newRes
        return res

    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        dp = [0for i in range(days[-1] + 1)]
        for i in range(days[-1] + 1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0,i-7)] + costs[1],dp[max(0,i-1)] + costs[0],dp[max(0,i-30)] + costs[2])
        return dp[-1]

    def countTriplets(self, A: 'List[int]') -> 'int':
        count = 0
        firstDic = {}
        secondDic = {}
        for i in range(len(A)):
            if A[i] not in firstDic:
                tempCount = 0
                for j in range(len(A)):
                    cur = A[i] & A[j]
                    if cur not in secondDic:
                        subTemp = 0
                        for k in range(len(A)):
                            if A[i] & A[j] & A[k] == 0:
                                subTemp += 1
                        secondDic[cur] = subTemp
                    tempCount += secondDic[cur]
                firstDic[A[i]] = tempCount
            count += firstDic[A[i]]
        return count




A = Solution()
print(A.countTriplets([2,1,3]))