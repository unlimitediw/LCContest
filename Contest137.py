import bisect
from collections import defaultdict


class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        stones.sort()
        while stones:
            if len(stones) == 1:
                return stones[0]
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 == stone_2:
                continue
            else:
                new_stone = stone_1 - stone_2
                stones.insert(bisect.bisect_left(stones, new_stone), new_stone)

        return 0

    def removeDuplicates(self, S: str) -> str:
        if len(S) == 1:
            return S
        cur_idx = 0
        while cur_idx < len(S) - 1:
            if S[cur_idx] == S[cur_idx + 1]:
                S = S[:cur_idx] + S[cur_idx + 2:]
                cur_idx = max(0, cur_idx - 1)
            else:
                cur_idx += 1
        return S

    def longestStrChain(self, words: list) -> int:

        def is_predecessor(word_1, word_2):
            for i in range(len(word_2) - 1):
                if word_1[i] != word_2[i]:
                    word_1 = word_1[:i] + word_2[i] + word_1[i:]
                    if word_1 == word_2:
                        return True
                    return False
            return True

        memo = defaultdict(list)
        word_dic = {}
        max_len = 0
        res = 1

        for word in words:
            max_len = max(max_len, len(word))
            memo[len(word)].append(word)

        for word in memo[1]:
            word_dic[word] = 1

        for i in range(2,max_len+1):
            for word in memo[i]:
                word_dic[word] = 1
                for pre in memo[i-1]:
                    if is_predecessor(pre,word):
                        word_dic[word] = max(word_dic[word],word_dic[pre] + 1)
                res = max(res,word_dic[word])

        return res

    def lastStoneWeightIIOld(self, stones: list) -> int:
        stones.sort()
        visited = {tuple(stones)}
        search = [stones]
        res = float('inf')
        count = 0
        while search:
            count += 1
            cur = search.pop()
            if len(cur) == 0:
                return 0
            elif len(cur) == 1:
                res = min(res,cur[0])
            else:
                for i in range(len(cur)):
                    for j in range(i+1,len(cur)):
                        stone_1 = cur[j]
                        stone_2 = cur[i]
                        new_stone = stone_1 - stone_2
                        new_stones = cur[:i] + cur[i+1:j] + cur[j+1:]
                        if new_stone != 0:
                            new_stones.insert(bisect.bisect_left(new_stones, new_stone), new_stone)
                        new_stones_tuple = tuple(new_stones)
                        if new_stones_tuple not in visited:
                            visited.add(new_stones_tuple)
                            search.append(new_stones)
        return res

    def lastStoneWeightII(self, stones: list) -> int:
        cur_list = {stones[0],-stones[0]}
        next_list = set()
        for i in range(1,len(stones)):
            for cur in cur_list:
                next_list.add(cur + stones[i])
                next_list.add(cur - stones[i])
            cur_list = next_list
            next_list = set()
        res = float('inf')
        for elem in cur_list:
            if elem >= 0:
                res = min(res,elem)
        return res
A = Solution()
# 30 bits
# each bits positive or negative
# result the answer
# mask
# must 1 positive 1 negative
# then new mask
# at most len times
# so it is 15 * 14 * 30
print(A.lastStoneWeightIIOld([1,1,2,3,55,2,82,98]))
print(A.lastStoneWeightII([1,1,2,3,55,82,2,98]))
