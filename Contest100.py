class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def checkSmall(R):
            pre = R[0]
            for i in range(1,len(R)):
                if pre > R[i]:
                    return False
                pre = R[i]
            return True

        return checkSmall(A) or checkSmall(A[::-1])

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        rootList = []
        def reconstruct(cur):
            if not cur:
                return
            reconstruct(cur.left)
            rootList.append(cur.val)
            reconstruct(cur.right)
        reconstruct(root)
        resRoot = rootList[0]
        iterRoot = TreeNode(resRoot)
        for i in range(1,len(rootList)):
            iterRoot.right = TreeNode(rootList[i])
            iterRoot = iterRoot.right
        return resRoot

    def subarrayBitwiseORsSlow(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic = {}
        def bitSum(curA):
            q = 0
            for elem in curA:
                q|= elem
            return q
        def checkSub(start):
            if start == len(A):
                return set()
            cur = set()
            for i in range(start + 1,len(A) + 1):
                if str(A[start:i]) not in dic:
                    cur.add(bitSum(A[start:i]))
            cur = cur.union(checkSub(start+1))
            return cur
        return len(checkSub(0))

    def subarrayBitwiseORsNSQU(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        resSet = set()
        n = len(A)
        for i in range(n):
            cur = A[i]
            resSet.add(cur)
            for j in range(i + 1,n):
                cur |= A[j]
                resSet.add(cur)
        return len(resSet)

    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = set()
        pre = set()
        for n in A:
            cur = {n}
            for p in pre:
                cur.add(p|n)
            pre = cur
            for p in pre:
                res.add(p)
        return len(res)

    def orderlyQueuePreK(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        def transform(St):
            return St[K:] + S[0:K]
        Smallest = S
        i = len(S)
        while i > 0:
            S = transform(S)
            print(S)
            Smallest = min(S,Smallest)
            i -= 1
        return Smallest

    def orderlyQueueStupid(self,S,K):
        def transform(St,pos):
            return St[:pos] + St[pos+1:] + St[pos]
        tolerance = 100
        min_res = S
        while True:
            max_idx = 0
            for i in range(1,K):
                if S[i] > S[max_idx]:
                    max_idx = i
            next = transform(S,max_idx)
            if next >= S:
                min_res = min(min_res,S)
                if tolerance < 0:
                    return min(S,min_res)
                else:
                    tolerance -= 1
                    S = next
            else:
                S = next





print(Solution().orderlyQueue("gxvz",4))

