import math


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for digit in A:
            if digit % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)
        return even + odd

    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        memo = []
        cur_1 = tree[0]
        cur_2 = None
        group_start = 0
        continuous_start = 0
        start = 0
        treeLength = len(tree)
        for i in range(treeLength):
            if tree[i] != cur_1:
                start = i
                continuous_start = i
                cur_2 = tree[i]
                break
            if i == treeLength - 1:
                return treeLength
        for i in range(start, treeLength):
            if tree[i] != cur_2 and tree[i] != cur_1:
                memo.append(i - group_start)
                cur_1 = tree[continuous_start]
                cur_2 = tree[i]
                group_start = continuous_start
                continuous_start = i
            elif tree[i] != tree[continuous_start]:
                continuous_start = i
            if i == treeLength - 1:
                memo.append(i + 1 - group_start)
        return max(memo)

    def sumSubarrayMinsPre(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        total = sum(A)
        min_memo = []
        pre = float('inf')
        for i in range(n - 1, -1, -1):
            pre = min(pre, A[i])
            min_memo.append(pre)
        min_memo = min_memo[::-1]
        for i in range(n):
            remain = n - i - 1
            cur = A[i]
            for j in range(1, remain + 1):
                if cur < min_memo[i + j]:
                    total += (remain - j + 1) * cur
                    break
                if A[i + j] < cur:
                    cur = A[i + j]
                total += cur
        return total % (10 ** 9 + 7)

    # use dp to solve the problem with left min and right min
    # solve the left min and right min problem with stack
    def sumSubarrayMins(self, A):
        n = len(A)
        memo = []
        total = 0
        # solve left min and right min
        for i in range(n):
            j = i
            while memo and A[i] < memo[-1][0]:
                cur = memo[-1]
                total += cur[0] * (i - cur[1]) * (cur[1] - cur[2] + 1)
                j = cur[2]
                memo.pop()
            memo.append([A[i], i, j])
        while memo:
            cur = memo[-1]
            total += cur[0] * (n - cur[1]) * (cur[1] - cur[2] + 1)
            memo.pop()
        return total % (10 ** 9 + 7)

    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        count = 0
        l, r = int(L), int(R)
        ac_l, ac_r = int(math.ceil(l ** 0.5)), int(r ** 0.5)
        a = [1,4,
             9,
             121,
             484,
             10201,
             12321,
             14641,
             40804,
             44944,
             1002001,
             1234321,
             4008004,
             100020001,
             102030201,
             104060401,
             121242121,
             123454321,
             125686521,
             400080004,
             404090404,
             10000200001,
             10221412201,
             12102420121,
             12345654321,
             40000800004,
             1000002000001,
             1002003002001,
             1004006004001,
             1020304030201,
             1022325232201,
             1024348434201,
             1210024200121,
             1212225222121,
             1214428244121,
             1232346432321,
             1234567654321,
             4000008000004,
             4004009004004,
             100000020000001,
             100220141022001,
             102012040210201,
             102234363432201,
             121000242000121,
             121242363242121,
             123212464212321,
             123456787654321,
             400000080000004,
             10000000200000001,
             10002000300020001,
             10004000600040001,
             10020210401202001,
             10022212521222001,
             10024214841242001,
             10201020402010201,
             10203040504030201,
             10205060806050201,
             10221432623412201,
             10223454745432201,
             12100002420000121,
             12102202520220121,
             12104402820440121,
             12122232623222121,
             12124434743442121,
             12321024642012321,
             12323244744232321,
             12343456865434321,
             12345678987654321,
             40000000800000004,
             40004000900040004]
        start = -1
        end = -1
        for i in range(len(a)):
            print(a[i])
            if start == -1:
                if l <= a[i]:
                    start = i
            else:
                if r < a[i]:
                    end = i - 1
                    break
            if i == len(a) - 1 and end == -1:
                end = len(a) - 1
        return end - start + 1

    def superpalindromesInRangeBru(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        count = 0
        l, r = int(L), int(R)
        ac_l, ac_r = int(math.ceil(l ** 0.5)), int(r ** 0.5)
        for i in range(ac_l, ac_r + 1):
            check = str(i)
            if check == check[::-1]:
                check2 = str(i ** 2)
                if check2 == check2[::-1]:
                    count += 1
                    print(check2)

        return count



print(Solution().superpalindromesInRange("38455498359",
"999999999999999999"))