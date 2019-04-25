class Solution:
    def __init__(self):
        self.hashSet = {}
    # part1
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

        str = bin(N)
        maxDist = 0
        curIdx = -1
        for i in range(len(str)):
            if str[i] == "1":
                if curIdx == -1:
                    curIdx = i
                else:
                    if i - curIdx > maxDist:
                        maxDist = i - curIdx
                    curIdx = i
        return maxDist

    # part2
    def reorderedPowerOf2old(self, N):
        """
        :type N: int
        :rtype: bool
        """
        powerList = []
        for i in range(32):
            powerList.append(2**i)
        numStr = str(N)
        print(powerList)
        numList = self.reorderList(numStr)
        for num in numList:
            if num[0] != '0':
                if int(num) in powerList:
                    return True
        return False

    def reorderList(self,numStr):
        k = 0
        for digit in numStr:
            k += 10**int(digit)
        if k in self.hashSet:
            return self.hashSet[k]
        else:
            returnList = []
            if len(numStr) == 1:
                return [numStr]
            for i in range(len(numStr)):
                for num in self.reorderList(numStr[:i]+numStr[i+1:]):
                    returnList.append(numStr[i] + num)
            self.hashSet[k] = returnList
            return returnList

    # part2 alter
    def reorderedPowerOf2(self, N):
        powerList = []
        strNum = str(N)
        for i in range(32):
            powerList.append(2**i)
        for powerNum in powerList:
            strPowerNum = str(powerNum)
            if len(strPowerNum) == len(strNum):
                copyStrNum = strNum
                for i in range(len(strPowerNum)):
                    findI = False
                    for j in range(len(copyStrNum)):
                        if strPowerNum[i] == copyStrNum[j]:
                            copyStrNum = copyStrNum[:j] + copyStrNum[j+1:]
                            findI = True
                            break
                    if not findI:
                        break
                    if i == len(strPowerNum) - 1:
                        return True
        return False

    # part3
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        BDic = {}
        for i in range(len(B)):
            if B[i] not in BDic:
                BDic[B[i]] = [i]
            else:
                BDic[B[i]].append(i)
        B.sort()

        rubbish = []

        Apos = 0
        for i in range(len(A)):
            while A[Apos] <= B[i]:
                rubbish.append(Apos)
                Apos += 1
                if Apos >= len(A):
                    break
                print(Apos,i,len(A),A[Apos],B[i])
            Apos += 1
            if Apos >= len(A):
                break
            print(Apos, i, len(A), A[Apos], B[i])

        newList = []
        actualI = 0
        ADic = {}
        for i in range(len(A)):
            if i not in rubbish:
                ADic[BDic[B[actualI]].pop(0)] = A[i]
                actualI += 1
        for i in range(len(A)):
            if i in ADic:
                newList.append(ADic[i])
            else:
                newList.append(A[rubbish.pop(0)])
        return newList

A =  [718967141,189971378,341560426,23521218,339517772]
B =  [967482459,978798455,744530040,3454610,940238504]
print(Solution().advantageCount(A,B))
