class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """

        res = ''
        cur = ''
        start = 0
        for i in range(len(S)):
            if S[i] == '(':
                if start > 0:
                    res += S[i]
                start += 1
            else:
                start -= 1
                if start > 0:
                    res += S[i]
        return res

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def find(cur,curRoot):
            cur += str(curRoot.val)
            res = 0
            if not curRoot.left and not curRoot.right:
                return int(cur,2)
            else:
                if curRoot.left:
                    res += find(cur,curRoot.left)
                if curRoot.right:
                    res += find(cur,curRoot.right)
                return res
        return find('',root)

    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        def check(cur):
            pos = 0
            for curPos in range(len(cur)):
                char = cur[curPos]
                if char == pattern[pos]:
                    pos += 1
                    if pos == len(pattern):
                        return curPos +1
                elif 97 > ord(char) or ord(char) > 122:
                    return -1
            return -1

        res = []
        for query in queries:
            pos = check(query)
            print(pos)
            if pos == -1:
                res.append(False)
            else:
                status = True
                for i in range(pos,len(query)):
                    if 97 > ord(query[i]) or ord(query[i]) > 122:
                        status = False
                        break
                res.append(status)
        return res

    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        if not clips:
            return -1
        dp = [0] * len(clips)
        dp[0] = 1
        clips.sort()
        if clips[0][0] > 0:
            return -1
        if clips[0][1] >= T:
            return 1
        for i in range(1,len(clips)):
            minV = float('inf')
            find = False
            for j in range(0,i):
                find = True
                if clips[j][1] >= clips[i][0]:
                    if clips[j][0] < clips[i][0]:
                        minV = min(minV,dp[j]+1)
                    else:
                        minV = min(minV,dp[j])
            dp[i] = minV
            if find:
                if clips[i][1] >= T:
                    return minV
        return -1


A = Solution()
print(A.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],9))