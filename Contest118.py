import math


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class NewTree(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.neighbour = None
        self.idx = None
        self.parent = None


class Node(object):
    def __init__(self,x):
        self.val = x
        self.idx = None
        self.left = None
        self.right = None


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = []
        if x == 1 and y == 1:
            if bound >= 2:
                return [2]
            else:
                return []
        elif y > x:
            temp = y
            y = x
            x = temp
        xub = int(math.log(bound, x))
        if y == 1:
            yub = 0
        else:
            yub = int(math.log(bound, y))
        for i in range(xub + 1):
            for j in range(yub + 1):
                cur = x ** i + y ** j
                if cur <= bound:
                    res.append(cur)
        return list(set(res))

    def pancakeSortAs1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # A star
        memo = {}
        visited = {tuple(A)}

        def conflict(check):
            up = True
            count = 0
            for i in range(1, len(A)):
                if up:
                    if check[i] < check[i - 1]:
                        count += 1
                        up = False
                else:
                    if check[i] > check[i - 1]:
                        count += 1
                        up = True
            return count

        if conflict(A) == 0:
            return []
        memo[conflict(A)] = [[A, []]]
        while memo:
            key = min(memo.keys())
            cur = memo[key].pop()
            if not memo[key]:
                memo.pop(key)
            cur_A = cur[0]
            for k in range(1, len(A) + 1):
                k_cur = cur_A[:k][::-1] + cur_A[k:]
                t_k_cur = tuple(k_cur)
                if t_k_cur in visited:
                    continue
                else:
                    visited.add(t_k_cur)
                    count = conflict(k_cur)
                    next = cur[1][:] + [k]
                    if count == 0:
                        print(k_cur)
                        return next
                    if count not in memo:
                        memo[count] = [[k_cur, next]]
                    else:
                        memo[count].append([k_cur, next])

    def pancakeSortAs2(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # A star
        visited = {tuple(A)}

        def conflict(check):
            up = True
            count = 0
            for i in range(1, len(A)):
                if up:
                    if check[i] < check[i - 1]:
                        count += 1
                        up = False
                else:
                    if check[i] > check[i - 1]:
                        count += 1
                        up = True
            return count

        if conflict(A) == 0:
            return []
        memo = [[A, []]]
        memo_next = []
        last = conflict(A)
        while memo:
            cur = memo.pop()
            cur_A = cur[0]
            for k in range(1, len(A) + 1):
                k_cur = cur_A[:k][::-1] + cur_A[k:]
                t_k_cur = tuple(k_cur)
                if t_k_cur in visited:
                    continue
                else:
                    visited.add(t_k_cur)
                    count = conflict(k_cur)
                    next = cur[1][:] + [k]
                    if count <= last:
                        if count == 0:
                            return next
                        if count == last:
                            memo_next.append([k_cur, next])
                        else:
                            last = count
                            memo_next = [[k_cur, next]]
            if not memo:
                memo = memo_next
                memo_next = []

    # 审题..permutation
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # 双反转
        res = []
        for i in range(len(A), -1, -1):
            for j in range(len(A)):
                if A[j] == i:
                    cur = j
                    break
            if cur < i - 1:
                res += [cur + 1, i]
                A = A[:cur + 1][::-1] + A[cur + 1:]
                A = A[:i][::-1] + A[i:]
        return res

    def flipMatchVoyageLR(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """

        def copyTree(curRoot):
            newRoot =  NewTree(curRoot.val)
            if curRoot.left:
                newRoot.left = copyTree(curRoot.left)
            if curRoot.right:
                newRoot.right = copyTree(curRoot.right)
            return newRoot

        def findNeighbour(curRoot):
            if curRoot.left and curRoot.right:
                curRoot.left.parent = curRoot
                curRoot.right.parent = curRoot
                curRoot.left.neighbour = curRoot.right
                curRoot.right.neighbour = curRoot.left
            if curRoot.left:
                findNeighbour(curRoot.left)
            if curRoot.right:
                findNeighbour(curRoot.right)

        newRoot = copyTree(root)
        findNeighbour(newRoot)

        res = []
        cur = []

        def constructCur(curRoot):
            curRoot.idx = len(cur)
            cur.append(curRoot)
            if curRoot.left:
                constructCur(curRoot.left)
            if curRoot.right:
                constructCur(curRoot.right)

        constructCur(newRoot)

        for i in range(len(voyage)):
            if voyage[i] != cur[i].val:
                if not cur[i].neighbour:
                    return [-1]
                neighbour = cur[i].neighbour
                if voyage[i] != neighbour.val or voyage[neighbour.idx] != cur[i].val:
                    return [-1]
                else:
                    res.append(cur[i].parent.idx + 1)
                    temp = cur[i].val
                    cur[i].val = neighbour.val
                    neighbour.val = temp
        return res

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.count = 0
        cur = []
        res = []
        def copyTree(curRoot):
            newRoot = Node(curRoot.val)
            cur.append(newRoot)
            newRoot.idx = self.count
            self.count += 1
            if curRoot.left:
                newRoot.left = copyTree(curRoot.left)
            if curRoot.right:
                newRoot.right = copyTree(curRoot.right)


        def dfs(node,provide,need):
            if node.val != need:
                return False
            else:
                if provide == voyage[node.idx]:
                    return True
                elif node.left and dfs(node.left,provide,voyage[node.idx]):
                    node.val = node.left.val
                    res.append(node.idx + 1)
                    return True
                elif node.right and dfs(node.right,provide,voyage[node.idx]):
                    node.val = node.right.val
                    res.append(node.idx + 1)
                    return True
                else:
                    return False
        copyTree(root)

        for i in range(len(voyage)):
            if cur[i].val != voyage[i] and not dfs(cur[i],cur[i].val,cur[i].val):
                return [-1]
        return res
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)

A = Solution()
print(A.flipMatchVoyageLR(T,[1,3,2]))
# print(len([5,7,6,10,9,10,9,10,7,10,9,10,5,10,9,10,7,10,9,6,10,9,10,5,9,10,6,10,9,10,6,10,5,10,9,10,7,10,9,10,5,10,9,10,7,6,10,9,10,5,10,9,10,6,10,9,10,6,10,9,10,6,10,9,5,10,9,10,6,9,10,7,10,9,10,5,10,6,10,9,10,6,10,9,10,6,10,9,10,5,10,9,10,7,10,9,6,10,5,10,9,10,7,10,9,10,5,10,9,8,10,6,5,4,5,6,5,6,7,6,7,6,4,6,7,6,5,7,8,7,8,7,6,5,7,8,7,8,7,6,7,6,4,6,7,6,7,8,6,8,7,6,7,6,5,4,6,7,6,7,6,5,6,5,4,2,10,6,7,6,7,6,5,4,6,7,6,7,6,5,6,5,3,10,9,10,7,8,7,8,7,6,5,7,8,7,8,7,6,7,6,4,6,7,6,7,8,6,10,8,10,5,6,5,6,7,6,7,6,10,9,10,6,7,6,7,6,4,10,9,8,4,5,3,5,6,5,6,5,4,3,10,6,7,6,7,6,4,10,9,10,6,7,5,4,7,8,7,8,7,6,5,7,8,7,8,7,6,7,6,5,3,4,6,7,6,7,8,7,8,7,5,7,8,7,6,8,7,6,7,6,5,4,6,7,6,7,6,5,6,5,4,2,10,9,10,7,8,7,8,7,6,5,7,8,7,8,7,6,7,6,5,4,3,10,9,10,6,7,6,7,6,5,4,6,7,6,7,6,5,6,5,3,10,9,10,7,8,7,8,7,6,5,7,8,7,8,7,5,4,10,9,10,3,5,6,5,6,5,10,9,8,10,6,7,6,7,6,4,6,7,6,5,7,8,7,8,7,6,5,7,8,7,8,7,6,7,6,4,6,7,6,7,8,6,10,9,10,4,5,4,5,6,5,6,5,10,9,8,10,4,6,7,6,7,6,10,9,4,5,4,3,10,7,8,7,8,7,6,5,7,8,7,8,7,4,3,10,9,10,5,6,5,6,5,4,5,4,10,9,10,8,9,8,9,8,7,6,8,9,8,9,8,7,8,7,6,4,5,7,8,7,8,9,8,9,8,6,8,9,8,7,9,8,7,8,7,6,5,7,8,7,8,7,6,7,6,5,4,3,6,7,6,7,8,7,8,7,4,7,8,7,8,7,5,7,8,6,8,9,8,9,8,7,6,8,9,8,9,8,7,8,7,5,7,8,7,8,9,7,9,8,7,8,7,6,5,7,8,7,8,7,6,7,6,5,3,4,6,7,6,7,8,7,8,7,5,7,8,7,6,8,7,6,7,6,5,4,6,7,6,7,6,5,6,5,4,3,2,10,9,10,7,8,7,8,7,6,5,7,8,7,8,7,6,7,6,5,3,4,6,7,6,7,8,7,8,7,5,7,8,7,6,8,7,6,7,6,5,4,6,7,6,7,6,5,6,5,4,2,10,9,10,7,8,7,8,7,6,5,7,8,7,8,7,6,7,6,5,4,3,10,9,10,6,7,6,7,6,5,4,6,7,6,7,6,5,6,5,3,10,9,10,7,8,7,8,7,6,5,7,8,7,8,7,5,4,10,9,10,3,5,6,5,6,5,10,9,3,4,3,2,10,8,9,8,9,8,7,6,8,9,8,9,8,7,8,7,6,4,5,7,8,7,8,9,8,9,8,6,8,9,8,7,9,8,7,8,7,6,5,7,8,7,8,7,3,10,9,10,5,6,5,6,5,4,5,4,10,9,3,4,3,4,5,3,9,8,4]))
