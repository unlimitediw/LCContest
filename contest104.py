class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dic = {}
        for i in range(len(deck)):
            if deck[i] not in dic:
                dic[deck[i]] = 1
            else:
                dic[deck[i]] += 1
        m_v = min(dic.values())
        for i in range(2,m_v+1):
            can = True
            for val in dic.values():
                if val % i != 0:
                    can = False
                    continue
            if can:
                return True
        return False

    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = []
        n = len(A)
        for k in range(2):
            if k == 1:
                A = A[::-1]
            min_map = [A[-1]]
            for i in range(n-2,-1,-1):
                min_map.append(min(min_map[-1],A[i]))
            min_map = min_map[::-1]
            cur = A[0]
            for i in range(1,n):
                cur = max(cur,A[i-1])
                if cur <= min_map[i]:
                    res.append(i)
                    break
        return min(res)

    def wordSubsetsInorder(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        bl = len(B)
        checkSet = [True for _ in range(len(A))]
        def checkSub(w1,w2):
            l1,l2 = len(w1),len(w2)
            if l2 > l1:
                return False
            for i in range(l1 - l2 + 1):
                if w1[i:l2 + i] == w2:
                    return True
            return False
        for i in range(len(A)):
            for j in range(bl):
                if not checkSub(A[i],B[j]):
                    checkSet[i] = False
                    break
        res = []
        for i in range(len(A)):
            if checkSet[i]:
                res.append(A[i])
        return res

    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        A_dic = []
        B_dic = []

        for a in A:
            new_dic = {}
            for char in a:
                if char not in new_dic:
                    new_dic[char] = 1
                else:
                    new_dic[char] += 1
            A_dic.append(new_dic)
        for b in B:
            new_dic = {}
            for char in b:
                if char not in new_dic:
                    new_dic[char] = 1
                else:
                    new_dic[char] += 1
            B_dic.append(new_dic)
        # actually, since it is unorder we can compress B
        B_monster = {}
        for b_subDic in B_dic:
            for key,val in b_subDic.items():
                if key not in B_monster:
                    B_monster[key] = val
                else:
                    B_monster[key] = max(B_monster[key],val)
        #check
        checkSet = [True for _ in range(len(A))]
        def checkSub(x):
            for key,value in B_monster.items():
                if key not in A_dic[x]:
                    return False
                elif A_dic[x][key] < value:
                    return False
            return True
        for i in range(len(A)):
            if not checkSub(i):
                checkSet[i] = False

        res = []
        for i in range(len(A)):
            if checkSet[i]:
                res.append(A[i])
        return res

    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        # min-max
        # q-learn
        # backtrack
        # all try

        # step 1, rank each node with priority
        rankDic = {}
        i = 0
        rankDic[i] = [0]
        curQueue = [0]
        nextQueue = []
        visited = {0}
        while curQueue:
            cur = curQueue.pop()
            for elem in graph[cur]:
                if elem not in visited:
                    visited.add(elem)
                    nextQueue.append(elem)
            if not curQueue:
                if nextQueue:
                    i+=1
                    curQueue = nextQueue
                    nextQueue = []
                    rankDic[i] = curQueue[:]
        print(rankDic)