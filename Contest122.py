class ListNode(object):
    def __init__(self,val,pre):
        self.val = val
        self.pre = pre

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        cur = 0
        for val in A:
            if val % 2 == 0:
                cur += val
        for query in queries:
            if A[query[1]] % 2 == 0:
                cur -= A[query[1]]
            A[query[1]] += query[0]
            if A[query[1]] % 2 == 0:
                cur += A[query[1]]
            res.append(cur)
        return res

    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        res = ''
        if not root:
            return res
        searchQueue = []
        def searchTree(curRoot,curNode):
            if not curRoot.left and not curRoot.right:
                searchQueue.append(curNode)
            else:
                if curRoot.left:
                    newNode = ListNode(curRoot.left.val,curNode)
                    searchTree(curRoot.left,newNode)
                if curRoot.right:
                    newNode = ListNode(curRoot.right.val,curNode)
                    searchTree(curRoot.right,newNode)
        originNode = ListNode(root.val,None)
        searchTree(root,originNode)
        while True:
            show = []
            for search in searchQueue:
                show.append(search.val)
            rankList = []
            for node in searchQueue:
                rankList.append(node.val)
            curMin = min(rankList)
            newQueue = []
            res += chr(curMin+97)
            for node in searchQueue:
                if node.val == curMin:
                    if not node.pre:
                        return res
                    nextNode = node.pre
                    newQueue.append(nextNode)
            searchQueue = newQueue

    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        iA = 0
        iB = 0
        res = []
        while iA < len(A) and iB < len(B):
            if A[iA].start < B[iB].start:
                if A[iA].end < B[iB].start:
                    iA += 1
                else:
                    if A[iA].end < B[iB].end:
                        res.append([B[iB].start,A[iA].end])
                        iA += 1
                    else:
                        res.append([B[iB].start,B[iB].end])
                        iB += 1
            else:
                if B[iB].end < A[iA].start:
                    iB += 1
                else:
                    if B[iB].end < A[iA].end:
                        res.append([A[iA].start,B[iB].end])
                        iB += 1
                    else:
                        res.append([A[iA].start,A[iA].end])
                        iA += 1
        return res

    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        # BFS
        leftSet = [] #(-inf,-1]
        rightSet = [] #[0,inf)
        queue = [[root,0]]
        nextQueue = []
        memoDic = {}
        while queue:
            cur = queue.pop()
            if cur[1] not in memoDic:
                memoDic[cur[1]] = [cur[0].val]
            else:
                memoDic[cur[1]].append(cur[0].val)
            if cur[0].left:
                nextQueue.append([cur[0].left,cur[1]-1])
            if cur[0].right:
                nextQueue.append([cur[0].right,cur[1]+1])
            if not queue:
                queue = nextQueue[:]
                nextQueue = []
                for key,val in memoDic.items():
                    val.sort()
                    if key >= 0:
                        if key >= len(rightSet):
                            rightSet.append(val)
                        else:
                            rightSet[key] += val
                    else:
                        key = - key - 1
                        if key >= len(leftSet):
                            leftSet.append(val)
                        else:
                            leftSet[key] += val
                memoDic = {}
        return leftSet[::-1] + rightSet




A = Solution()
