class Solution:
    def largeGroupPositions(self, S: 'str') -> 'List[List[int]]':
        res = []
        cur = ''
        count = 0
        for i in range(len(S)):
            if S[i] == cur:
                count += 1
            else:
                cur = S[i]
                if count >= 2:
                    res.append([i - count-1, i - 1])
                count = 0
        if count >= 2:
            res.append([len(S) - 1 - count, len(S) - 1])
        return res

    def maskPII(self, S: 'str') -> 'str':
        if '@' in S:
            cur = S.lower().split('@')
            left, right = cur[0],cur[1]
            left = left[0] + '*****' + left[-1] + '@'
            return left + right
        else:
            acNum = ''
            for c in S:
                if 48 <= ord(c) < 58:
                    acNum += c
            if len(acNum) == 10:
                return '***-***-' + acNum[-4:]
            else:
                remain = len(acNum) - 10
                add = ''
                for i in range(remain):
                    add += '*'
                return '+' + add + '-***-***-' + acNum[-4:]

    def consecutiveNumbersSum(self, N: 'int') -> 'int':
        '''
        we should use dp to solve this problem
        
        :param N:
        :return:
        '''


A = Solution()


