class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        A.sort()
        for i in range(len(A)):
            if K == 0:
                break
            if A[i] < 0:
                A[i] = -A[i]
            else:
                if K % 2 == 0:
                    return sum(A)
                else:
                    return sum(A) - 2 * min(A)
            K -= 1
        return sum(A)

    def clumsyOld(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        elif N == 2:
            return 2

        res = -2
        other = (N - 2) % 4

        if other == 3:
            res += N // (N - 1) + (N - 2)
        elif other == 2:
            res += N + (N - 1)
        elif other == 1:
            res += N

        if N > 5:
            res += N * (N - 1) // (N - 2) + (N - 3)
            N -= 4
        while N > 5:
            res -= N * (N - 1) // (N - 2) - (N - 3)
            N -= 4
        return res

    def clumsy(self, N):
        count = 0
        cur = 0
        res = 0
        # first loop
        while N > 0:
            if count == 0:
                cur += N
            elif count == 1:
                cur *= N
            elif count == 2:
                cur //= N
            elif count == 3:
                res += N
                count = 0
                N -= 1
                break
            N -= 1
            count += 1
        res += cur
        cur = 0
        while N > 0:
            if count == 0:
                cur += N
            elif count == 1:
                cur *= N
            elif count == 2:
                cur //= N
                res -= cur
                cur = 0
            else:
                res += N
                count = -1
            N -= 1
            count += 1
        res -= cur
        return res

    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        check = [True for _ in range(6)]
        for i in range(len(A)):
            for j in range(len(check)):
                if check[j]:
                    if j + 1 != A[i] and j + 1 != B[i]:
                        check[j] = False
        newCheck = []
        for i in range(len(check)):
            if check[i]:
                newCheck.append(i + 1)
        if not newCheck:
            return -1
        countAB = []
        for val in newCheck:
            cur = [0, 0]
            for i in range(len(A)):
                if A[i] == val:
                    cur[0] += 1
                if B[i] == val:
                    cur[1] += 1
            countAB.append(cur)
        res = float('inf')
        for count in countAB:
            res = min(res, min(count) + len(A) - sum(count))
        return res

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        memo = [root]
        for i in range(1, len(preorder)):
            pre = memo[-1]
            cur = TreeNode(preorder[i])
            if cur.val < pre.val:
                pre.left = cur
                memo.append(cur)
            else:
                while len(memo) > 0:
                    if len(memo) == 1:
                        pre.right = cur
                        memo.pop()
                        memo.append(cur)
                        break
                    elif cur.val > memo[-2].val:
                        memo.pop()
                        pre = memo[-1]
                    else:
                        pre.right = cur
                        memo.pop()
                        memo.append(cur)
                        break
        return root


A = Solution()
print(A.minDominoRotations([2,1,2,4,2,2],
                           [5, 2, 6, 2, 3, 2]))
