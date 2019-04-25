class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.val = 1


    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        self.val += 1
        height = 0
        remain = 0
        for i in range(20):
            if self.val > 2**i - 1:
                height = i
                remain = self.val - (2**(i-1) - 1) + 1
                break
        cur = self.root
        search = 1
        while search < height:
            if remain > 2**(height - search):
                remain = remain - 2**(height - search)
                cur = self.root.right
            else:
                cur = self.root.left
            search += 1
        return cur


    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        repre = ''
        memo = []
        for i in range(len(S)):
            if 97 <= ord(S[i]) < 123 or 65 <= ord(S[i]) < 91:
                repre += S[i]
            else:
                memo.append((S[i], i))
        repre = repre[::-1]
        for elem in memo:
            idx = elem[1]
            repre = repre[0:idx] + elem[0] + repre[idx:]
        return repre

    def maxSubarraySumCircularSlow(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        lineA = A + A
        maxVal = -float('inf')
        for length in range(1, n + 1):
            preVal = sum(lineA[0:length])
            maxVal = max(preVal, maxVal)
            for pos in range(1, n):
                preVal += lineA[pos + length - 1] - lineA[pos - 1]
                maxVal = max(preVal, maxVal)
        return maxVal

    def maxSubarraySumCircularErr(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        lineA = A + A

        def withoutCir(lineA):
            maxVal = -float('inf')
            cur = 0
            curLength = 0
            curN = len(lineA)
            for i in range(curN):
                if lineA[i] < 0:
                    maxVal = max(maxVal, cur)
                    minus = lineA[i]
                    while i + 1 < curN and lineA[i+1] < 0:
                        i += 1
                        minus += lineA[i]
                        curLength += 1
                    # 此处cur继承没处理好
                    cur += minus


                    curLength += 1
                else:
                    if curLength < n:
                        cur += lineA[i]
                        curLength += 1
                    else:
                        maxVal = max(maxVal, cur)
                        cur += lineA[i]
                        cur -= lineA[i - n + 1]
            return maxVal

    def maxSubarraySumCircularLeft(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        lineA = A + A
        maxVal = -float('inf')
        minusDic = {}
        for i in range(2*n):
            if lineA[i] < 0:
                minus = lineA[i]
                curIdx = i
                while i + 1 < 2*n and lineA[i + 1] < 0:
                    i += 1
                    minus += lineA[i]
                minusDic[curIdx] = minus
        return 0

    def maxSubArray(self, nums):
        max_ending_here = max_so_far = nums[0]
        for n in nums[1:]:
            max_ending_here = max(n, max_ending_here + n)
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far
    def maxSubarraySumCircular(self, a):
        max_kadane = self.maxSubArray(a)
        if max_kadane < 0:
            return max_kadane
        max_wrap = sum(a)
        for i in range(len(a)):
            a[i] = -a[i]
        max_wrap = max_wrap + self.maxSubArray(a)
        if max_wrap > max_kadane:
            return max_wrap
        else:
            return max_kadane

