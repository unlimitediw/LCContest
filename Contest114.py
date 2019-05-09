class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        map = {}
        for i in range(26):
            map[order[i]] = chr(97 + i)
        print(map)
        for i in range(len(words)):
            newW = ''
            for c in words[i]:
                newW += map[c]
            words[i] = newW
        if words == sorted(words):
            return True
        return False

    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        A.sort()
        neg = []
        pos = []
        for i in range(len(A)):
            if A[i] >= 0:
                neg = A[:i][::-1]
                pos = A[i:]
                break
            if i == len(A) - 1:
                neg = A[::-1]
        if len(neg) % 2 != 0 or len(pos) % 2 != 0:
            return False
        for testL in [pos, neg]:
            if testL:
                stack = [testL[0]]
                for i in range(1, len(testL)):
                    if stack and testL[i] == 2 * stack[0]:
                        stack.pop(0)
                    else:
                        stack.append(testL[i])
                if stack:
                    return False
        return True

    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        memo = 0
        idx = 0
        maxLen = 0
        for word in A:
            maxLen = max(len(word), maxLen)
        maxMemo = ['' for _ in range(len(A))]
        while idx < maxLen:
            cur = ''
            firstMask = ''
            add = False
            for i in range(len(A)):
                if len(A[i]) > idx:
                    if maxMemo[i] > firstMask:
                        firstMask = maxMemo[i]
                        cur = A[i][idx]
                    else:
                        if A[i][idx] >= cur:
                            cur = A[i][idx]
                        else:
                            memo += 1
                            add = True
                            break
            if not add:
                for i in range(len(A)):
                    if len(A[i]) > idx:
                        maxMemo[i] += A[i][idx]
            idx += 1
        return memo


A = Solution()
print(A.minDeletionSize( ["ca","bb","ac"]))
