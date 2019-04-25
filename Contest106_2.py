import math
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddList = []
        evenList = []
        res = []
        for val in A:
            if val % 2 == 1:
                oddList.append(val)
            else:
                evenList.append(val)
        for i in range(len(oddList)):
            res.append(oddList[i])
            res.append(evenList[i])
        return res

    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        count = 0
        pre = 0
        for i in range(len(S)):
            if S[i] == '(':
                pre += 1
            else:
                if pre > 0:
                    pre -= 1
                else:
                    count += 1
        count += pre
        return count

    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        def compond(e,t):
            return math.factorial(t) / math.factorial(t-e) / math.factorial(e)
        valDic = {}
        resList = set()
        res = 0
        for val in A:
            if val not in valDic:
                valDic[val] = 1
            else:
                valDic[val] += 1
        keyList = list(valDic.keys())
        n = len(keyList)
        for i in range(n):
            for j in range(i,n):
                newT = target - keyList[i] - keyList[j]
                if newT in valDic:
                    valDic[keyList[i]] -= 1
                    valDic[keyList[j]] -= 1
                    valDic[newT] -= 1
                    if valDic[newT] >= 0 and valDic[keyList[i]] >= 0 and valDic[keyList[j]] >= 0:
                        resList.add(tuple(sorted([keyList[i],keyList[j],newT])))
                    valDic[keyList[i]] += 1
                    valDic[keyList[j]] += 1
                    valDic[newT] += 1
        resList = list(resList)
        for i in range(len(resList)):
            if resList[i][0] == resList[i][1]:
                if resList[i][1] == resList[i][2]:
                    res += compond(3,valDic[resList[i][0]])
                else:
                    res += compond(2,valDic[resList[i][0]]) * valDic[resList[i][2]]
            else:
                if resList[i][1] == resList[i][2]:
                    res += compond(2,valDic[resList[i][1]]) * valDic[resList[i][0]]
                else:
                    res += valDic[resList[i][0]] * valDic[resList[i][1]] * valDic[resList[i][2]]

        return int(res % (10**9+7))



print(Solution().threeSumMulti([2,1,1,2,2,2],5))