class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        checkSet = set()
        for email in emails:
            actual = ''
            for i in range(len(email)):
                if email[i] == '+':
                    while email[i] != '@':
                        i += 1
                if email[i] == '@':
                    actual += email[i+1:]
                    if actual not in checkSet:
                        checkSet.add(actual)
                    break
                elif email[i] == '.':
                    continue
                else:
                    actual += email[i]
        return len(checkSet)

    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        oneDic = {}
        zeroCount = 0
        res = 0
        for i in range(len(A)):
            if A[i] == 1:
                oneDic[i] = zeroCount
                zeroCount = 0
            else:
                zeroCount += 1
        if S == 0:
            valueList = list(oneDic.values())
            valueList.append(zeroCount)
            for val in valueList:
                res += val * (val + 1) // 2
            return res
        keyList = sorted(list(oneDic.keys()))
        m = len(keyList)
        endIdx = S - 1
        startIdx = 0
        if S > m:
            return 0
        while endIdx < m:
            if endIdx == m - 1:
                res += (oneDic[keyList[startIdx]] + 1) * (len(A) - keyList[endIdx])
            else:
                res += (oneDic[keyList[startIdx]] + 1) * (keyList[endIdx+1] - keyList[endIdx])
            startIdx += 1
            endIdx += 1
        return res

    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        height = len(A)
        width = len(A[0])
        dp = [[0 for _ in range(width)] for _ in range(height)]
        dp[0][0] = A[0][0]
        def getMinDp(h_idx,w_idx):
            res = dp[h_idx-1][w_idx]
            if w_idx - 1 >= 0:
                res = min(res,dp[h_idx-1][w_idx-1])
            if w_idx + 1 < width:
                res = min(res,dp[h_idx-1][w_idx+1])
            return res
        for w_idx in range(width):
            dp[0][w_idx] = A[0][w_idx]
        for h_idx in range(1,height):
            for w_idx in range(width):
                dp[h_idx][w_idx] = A[h_idx][w_idx] + getMinDp(h_idx,w_idx)
        return min(dp[-1])

    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """

        for _ in range(N):
            n = int(input())
            x = [int(q) for q in input().split()]
            a0 = x.count(0)
            a1 = x.count(1)
            am = x.count(-1)
            b = n - (a0 + a1 + am)
            print('no' if (b > 1) or (am > 0 and b) or (am > 1 and a1 == 0) else 'yes')

print(Solution().numSubarraysWithSum([0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0],
3))
