class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        buttom = 0
        left = 0
        right = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                buttom += 1 if grid[i][j] != 0 else 0
            left += max(grid[i])
        for j in range(len(grid[0])):
            maxVal = -float('inf')
            for i in range(len(grid)):
                if grid[i][j] > maxVal:
                    maxVal = grid[i][j]
            right += maxVal
        return left + right + buttom

    def numRescueBoatsSlow(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        res = 0
        count = 0
        remain = limit
        n = len(people)
        while True:
            if n <= 0:
                break
            if count == 0:
                remain = limit
                res += 1
                count = 1
                remain -= people.pop()
                n -= 1
            else:
                count = 0
                if people[0] > remain:
                    continue
                for i in range(n-1,-1,-1):
                    if people[i] <= remain:
                        people.pop(i)
                        n -= 1
                        i -= 1
                        break
        return res


    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        res = 0
        people = sorted(people)[::-1]
        corre = []
        remain = len(people)
        for person in people:
            corre.append(limit - person)
        for person in people:
            if remain <= 0:
                return res
            if person > corre[-1]:
                remain -= 1
            else:
                corre.pop()
                remain -= 2
            res += 1
        return res

    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        strList = []
        timesList = []
        targetList = []
        cur = ''
        target = -1
        for i in range(len(S)):
            if 65 <= ord(S[i]) <= 90 and 97 <= ord(S[i]) <= 122:
                strList.append(cur)
                timesList.append(int(S[i]))
            else:
                cur += S[i]
                if i == len(S) - 1:
                    strList.append(cur)
                    timesList.append(1)
        for i in range(len(timesList)):
            if i == 0:
                targetList.append(timesList[i] * len(strList[i]))
            else:
                targetList.append(timesList[i] * (len(strList[i]) + targetList[i-1]))
        for i in range(len(targetList)):
            if K < targetList[i]:
                if i == 0:
                    return strList


print(ord('A'))


print(Solution().numRescueBoats([1,2],3))