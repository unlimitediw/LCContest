class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestTimeFromDigits(self, A: list) -> str:
        A.sort()
        for cur in [2,1,0]:
            L1 = A[:]
            if cur in L1:
                L1.remove(cur)
                if cur == 2:
                    search = range(3,-1,-1)
                else:
                    search = range(9,-1,-1)
                for i in search:
                    if i in L1:
                        L1.remove(i)
                        if L1[0] < 6:
                            if L1[1] < 6:
                                return str(cur) + str(i) + ':' + str(L1[1]) + str(L1[0])
                            else:
                                return str(cur) + str(i) + ':' + str(L1[0]) + str(L1[1])
                        break

        return ''

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        def dfs(node1,node2,inverse):
            if not node1 and not node2:
                return True
            elif node1 and node2:
                if node1.val != node2.val:
                    return False
                if not inverse:
                    return (dfs(node1.left,node2.left,False) or dfs(node1.left,node2.left,True)) and \
                           (dfs(node1.right,node2.right,False) or dfs(node1.right,node2.right,True))
                else:
                    return (dfs(node1.left,node2.right,False) or dfs(node1.left,node2.right,True)) and \
                           (dfs(node1.right,node2.left,False) or dfs(node1.right,node2.left,True))
            else:
                return False

        return dfs(root1,root2,True) or dfs(root1,root2,False)

    def deckRevealedIncreasing(self, deck: list) -> list:
        res = []
        if not deck:
            return res
        deck.sort()

        if len(deck) % 2 == 0:
            sure = deck[:len(deck) // 2]
            next = self.deckRevealedIncreasing(deck[len(deck)//2:])
        else:
            sure = deck[:(len(deck) + 1)//2]
            next = self.deckRevealedIncreasing(deck[(len(deck)+1)//2:])
            if next:
                next.insert(0, next.pop())
        for i in range(len(sure)):
            res.append(sure[i])
            if i < len(next):
                res.append(next[i])
        return res


A = Solution()
print(A.largestTimeFromDigits([0,0,0,0]))