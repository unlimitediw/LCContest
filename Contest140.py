from collections import defaultdict
import bisect
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list:
        str_list = text.split()
        res = []
        for i in range(len(str_list) - 2):
            if str_list[i] == first and str_list[i+1] == second:
                res.append(str_list[i+2])
        return res

    def numTilePossibilities(self, tiles: str) -> int:


        res = set()
        def search(remain,pre):
            for i in range(len(remain)):
                cur = pre+remain[i]
                res.add(cur)
                search(remain[:i] + remain[i+1:],cur)
        search(tiles,'')
        return len(res)

    def numTilePossibilities_math(self, tiles: str) -> int:
        fact = [1]
        for i in range(1,8):
            fact += [fact[-1]*i]
        count = defaultdict(int)
        for i in tiles:
            count[i] += 1
        count = list(count.values())
        comb = [[0 for i in count]]
        cur = comb
        res = 0
        for k in range(1,len(tiles)+1):
            tmp = []
            for l in cur:
                for i in range(len(count)):
                    new_l = [i for i in l]
                    if new_l[i] < count[i]:
                        new_l[i] += 1
                        tmp += [tuple(new_l)]
            cur = set(tmp)
            for pair in cur:
                prod = 1
                for i in pair:
                    prod *= fact[i]
                res += fact[sum(pair)] / prod
        return int(res)

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        def search(node,inherit):
            if node:
                if not node.left and not node.right:
                    if node.val + inherit >= limit:
                        return node
                else:
                    left = search(node.left,inherit + node.val)
                    right = search(node.right,inherit + node.val)
                    cur = TreeNode(node.val)
                    if not left and not right:
                        return None
                    if left:
                        cur.left = left
                    if right:
                        cur.right = right
                    return cur
            else:
                return None

        res = search(root,0)
        return res

    def smallestSubsequence(self, text: str) -> str:
        pos = defaultdict(list)
        for i, char in enumerate(text):
            pos[char].append(i)

        result = []
        while pos:
            minLastIndex, char = min([(v[-1], k) for k, v in pos.items()])

            i = minLastIndex
            for k, v in pos.items():
                if k <= char and v[0] < minLastIndex:
                    i, char = v[0], k

            result.append(char)
            pos.pop(char)

            for k in pos:
                pos[k] = pos[k][bisect.bisect(pos[k], i):]

        return "".join(result)


A = Solution()
print(A.smallestSubsequence("cdadabcc"))