import collections
class Solution:
    def shortestToChar(self, S: str, C: str) -> list:
        memo = []
        for i in range(len(S)):
            if S[i] == C:
                memo.append(i)
        res = [float('inf')] * len(S)
        cur = 0
        for i in range(len(S)):
            if i > memo[cur]:
                if cur < len(memo) - 1:
                    cur += 1
            res[i] = min(res[i],abs(i - memo[cur]))
            if cur > 0:
                res[i] = min(res[i],abs(i-memo[cur-1]))
        return

    def flipgame(self, fronts: list, backs: list) -> int:
        same_set = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same_set.add(fronts[i])
        for val in sorted(list(set(fronts + backs))):
            if val not in same_set:
                return val
        return 0

    def minimumLengthEncoding(self, words: list) -> int:
        reverse_words = []
        for word in words:
            reverse_words.append(word[::-1])
        reverse_words.sort()
        res = 0
        cur = reverse_words[0]
        for i in range(1,len(reverse_words)):
            if cur != reverse_words[i][:len(cur)]:
                res += len(cur) + 1
            cur = reverse_words[i]
        res += len(reverse_words[-1]) + 1
        return res

    def numFactoredBinaryTrees(self, A: list) -> int:
        MODULE = 10 ** 9 + 7
        A.sort()
        dp = [1] * len(A)
        multi_map = collections.defaultdict(list)
        compare = set(A)
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i] * A[j] in compare:
                    multi_map[A[i]*A[j]].append([i,j])
        for i in range(len(A)):
            cur = 1
            if A[i] in multi_map:
                for pair in multi_map[A[i]]:
                    cur += dp[pair[0]] * dp[pair[1]]
            dp[i] = cur
        return sum(dp) % MODULE


A = Solution()
print(A.numFactoredBinaryTrees([2, 4]))
