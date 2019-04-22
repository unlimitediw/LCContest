class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        cur = ''
        finalRes = []
        for i in range(len(A)):
            cur += str(A[i])
            res = int(cur, 2)
            if res % 5 == 0:
                finalRes.append(True)
            else:
                finalRes.append(False)
        return finalRes

    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return '0'
        res = ''
        while N:
            if N % 2 == 1:
                res += '1'
                N = (N - 1) / -2
            else:
                res += '0'
                N /= -2

        return res

    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """

        if not head:
            return []
        memo = [head.val]
        while head.next:
            head = head.next
            memo.append(head.val)
        stack = [0]
        res = [0] * len(memo)
        for i in range(1, len(memo)):
            while memo[stack[-1]] < memo[i]:
                res[stack[-1]] = memo[i]
                stack.pop(-1)
                if not stack:
                    break
            stack.append(i)
        return res

    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        waitList = []
        visited = set()
        self.count = 0
        for i in range(len(A)):
            visited.add((i, 0))
            visited.add((i, len(A[0]) - 1))
            if A[i][0] == 1:
                waitList.append((i,0))
                self.count += 1
            if A[i][-1] == 1:
                waitList.append((i,len(A[0]) - 1))
                self.count += 1
        for i in range(1,len(A[0])-1):
            visited.add((0,i))
            visited.add((len(A)-1,i))
            if A[0][i] == 1:
                waitList.append((0,i))
                self.count += 1
            if A[len(A)-1][i] == 1:
                waitList.append((len(A)-1,i))
                self.count += 1
        def check(point):
            if point not in visited and 0 <= point[0] < len(A) and 0 <= point[1] < len(A[0]):
                visited.add(point)
                if A[point[0]][point[1]] == 1:
                    self.count += 1
                    return True
            return False
        def search(point):
            if check((point[0]+1,point[1])): search((point[0]+1,point[1]))
            if check((point[0]-1,point[1])): search((point[0]-1,point[1]))
            if check((point[0],point[1]+1)): search((point[0],point[1]+1))
            if check((point[0],point[1]-1)): search((point[0],point[1]-1))
        for elem in waitList:
            search(elem)
        total = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                total += A[i][j]
        return total - self.count

A = Solution()
print(A.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
