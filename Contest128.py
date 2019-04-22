class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        a = bin(N)
        a = a[2:]
        b = ''
        for char in a:
            if char == '0':
                b += '1'
            else:
                b += '0'
        return int(b, 2)

    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        dic = {}
        dic[0] = 0
        dic[30] = 0
        for point in time:
            cur = point % 60
            if cur not in dic:
                dic[cur] = 1
            else:
                dic[cur] += 1
        res = dic[0] * max(dic[0]-1,0) // 2 + dic[30] * max(dic[30]-1,0) // 2
        for key in dic.keys():
            if key < 30 and 60 -key in dic:
                res += dic[key] * dic[60-key]
        return res

    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """

        def check(least):
            remain = D
            cur = least
            pos = 0
            while remain > 0:
                if cur >= weights[pos]:
                    cur -= weights[pos]
                else:
                    remain -= 1
                    cur = least
                    pos -= 1
                if pos == len(weights) - 1:
                    return True
                pos += 1
            return False

        minL = max(weights)
        maxL = sum(weights)
        while minL < maxL:
            cur = (minL + maxL) // 2
            if check(cur):
                maxL = cur
            else:
                minL = cur + 1
        return minL

    def numDupDigitsAtMostNtest(self, N):
        """
        :type N: int
        :rtype: int
        """

        def check(num):
            cur = str(num)
            memo = [0] * 10
            for char in cur:
                memo[ord(char) - 48] += 1
                if memo[ord(char) - 48] == 2:
                    return True
            return False
        total = 0
        for i in range(1,N + 1):
            if check(i):
                total += 1
                #print(i)
        return total

    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 9位之后肯定重复，不重复的比重复少很多。
        def C(n,k):
            if k == 0:
                return 1

            return n * C(n-1,k-1)
        if N < 10:
            return 0
        N = str(N)
        res = 0
        for k in range(len(N) - 1):
            res += 9 * C(9,k)
        digits = [int(char) for char in N]
        #头部另算
        res += (digits[0] - 1) * C(9,len(N)-1)
        dSet = {digits[0]}
        idx = 1
        for d in digits[1:]:
            idx += 1
            nchoice = d - sum(x < d for x in dSet) # num of repeated digit correspond to head
            res += nchoice * C(10-idx,len(N)-idx)
            if d in dSet:
                break
            dSet.add(d)
        else:
            res += 1
        return res
        # 加入dp
        # 大于 10**k - 1
        # 则新的为旧的



A = Solution()
print('t',A.numDupDigitsAtMostN(999999999999999999999))
N = 0
