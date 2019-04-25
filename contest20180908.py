import collections
class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.remain = 0
        self.memo = 0
        self.numsDic = {}
        self.order = collections.deque()
        for i in range(0,len(A),2):
            if A[i] == 0:
                continue
            self.remain += A[i]
            if A[i+1] not in self.numsDic:
                self.numsDic[A[i+1]] = collections.deque([A[i]])
            else:
                self.numsDic[A[i+1]].append(A[i])
            self.order.append(A[i+1])

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > self.remain:
            return -1
        else:
            while True:
                if not self.order:
                    return -1
                cur = self.order[0]
                if self.numsDic[cur][0] > n:
                    self.numsDic[cur][0] -= n
                    return cur
                elif self.numsDic[cur][0] == n:
                    self.numsDic[cur].popleft()
                    self.order.popleft()
                    return cur
                elif n <= self.remain:
                    n -= self.numsDic[cur][0]
                    self.order.popleft()
                    self.numsDic[cur].popleft()
                else:
                    self.order.popleft()
                    return -1
            self.remain -= n


class StockSpanner(object):

    def __init__(self):
        pass

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """


A = RLEIterator([3,8,0,9,2,5])
print(A.next(2))
print(A.next(1))
print(A.next(1))
print(A.next(2))
