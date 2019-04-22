class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """

        check = set()

        def little(val):
            if val == 1 or val in check:
                return False
            for x in range(1, val):
                if val % x == 0:
                    if not little(val - x):
                        return True
            check.add(val)
            return False

        return little(N)

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def little(node, minV, maxV):
            local = max(abs(minV - node.val), abs(maxV - node.val))
            minV = min(node.val, minV)
            maxV = max(node.val, maxV)
            if node.left:
                local = max(local, little(node.left, minV, maxV))
            if node.right:
                local = max(local, little(node.right, minV, maxV))
            return local

        res = 0
        if root.left:
            res = max(res, little(root.left, root.val, root.val))
        if root.right:
            res = max(res, little(root.right, root.val, root.val))
        return res

    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxV = 2
        dp = [{} for _ in range(len(A))]
        for i in range(1, len(A)):
            curDic = {}
            for j in range(i):
                if j == 0:
                    if A[i] - A[0] not in curDic:
                        curDic[A[i] - A[0]] = 2
                else:
                    curJVal = 1
                    if A[i] - A[j] in dp[j]:
                        curJVal = dp[j][A[i] - A[j]]
                    if A[i] - A[j] not in curDic:
                        curDic[A[i] - A[j]] = curJVal + 1
                    else:
                        curDic[A[i] - A[j]] = max(curDic[A[i] - A[j]], curJVal + 1)
                    if curDic[A[i] - A[j]] > maxV: maxV = curDic[A[i] - A[j]]
            dp[i] = curDic
        return maxV

    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        if not S:
            return None
        D = 0
        val = ''
        Dmode = True
        ref = []

        for i in range(len(S)):
            if Dmode:
                if S[i] == '-':
                    D += 1
                else:
                    Dmode = False
                    val += str(S[i])
            else:
                if S[i] == '-':
                    ref.append((D, int(val)))
                    Dmode = True
                    val = ''
                    D = 1
                else:
                    val += str(S[i])
        ref.append((D, int(val)))

        Origin = TreeNode(ref[0][1])
        self.cur = None
        ref = ref[1:]
        def build(root, depth):
            if not ref:
                return -1
            self.cur = ref.pop(0)
            memo = -1
            if self.cur[0] == depth:
                root.left = TreeNode(self.cur[1])
                memo = build(root.left, depth + 1)
            elif self.cur[0] < depth:
                return self.cur[0]
            if memo == depth:
                root.right = TreeNode(self.cur[1])
                memo = build(root.right, depth + 1)
            return memo
        build(Origin,1)

        return Origin

A = Solution()

this = A.recoverFromPreorder("1-2--3---4-5--6---7")
print(this.left.left.left.val)
