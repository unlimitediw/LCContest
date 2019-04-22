class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        target = sum(A) / 3
        memo = 0
        time = 0
        for val in A:
            memo += val
            if memo == target:
                time += 1
                memo = 0
        if time == 3:
            return True
        return False

    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        cur = 0
        # method1
        for i in range(1000):
            cur += 10**i
            if cur % K == 0:
                print(len(str(cur)),K)
                return i+1
        # method2
        if str(K)[-1] in ['1','3','7','9']:
            return 1
        for i in range(10)
        return -1

A = Solution()
#print(A.smallestRepunitDivByK(1))

for i in range(1,10000):
    A.smallestRepunitDivByK(i)