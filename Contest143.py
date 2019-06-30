import collections


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list:
        N = num_people
        adder = [k + 1 for k in range(N)]
        sum_adder = sum(adder)
        res = [0 for _ in range(N)]
        mul = 0
        while mul * (mul + 1) // 2 * N ** 2 + (mul + 1) * sum_adder <= candies:
            for i in range(len(res)):
                res[i] += adder[i] + N * mul
            mul += 1
        remain = candies - sum(res)
        for i in range(len(res)):
            if remain > mul * N + i + 1:
                res[i] += mul * N + i + 1
                remain -= mul * N + i + 1
            else:
                res[i] += remain
                break
        return res

    def pathInZigZagTree(self, label: int) -> list:
        layer = 0
        while label > 2 ** layer - 1:
            layer += 1
        res = [label]
        pre = label
        while layer > 1:
            offset = (2 ** layer - 1) - pre
            pre = 2 ** (layer - 2) + offset // 2
            res.append(pre)
            layer -= 1
        return res[::-1]

    def minHeightShelvesSlow(self, books: list, shelf_width: int) -> int:
        if len(books) == 1:
            return books[0][1]
        N = len(books)
        memo = collections.defaultdict(list)
        memo[books[0][1]] = [[0, shelf_width - books[0][0], books[0][1]]]
        while memo:
            # print(memo)
            min_key = min(memo.keys())
            cur = memo[min_key]
            del memo[min_key]
            for i in range(len(cur)):
                idx = cur[i][0]
                if idx == N - 1:
                    return min_key
                if books[idx + 1][0] <= cur[i][1]:
                    memo[max(min_key, min_key + books[idx + 1][1] - cur[i][2])].append(
                        [idx + 1, cur[i][1] - books[idx + 1][0], max(cur[i][2], books[idx + 1][1])])
                memo[min_key + books[idx + 1][1]].append([idx + 1, shelf_width - books[idx + 1][0], books[idx + 1][1]])

    def minHeightShelvesGreedy(self, books: list, shelf_width: int) -> int:
        pre = {}
        # pre[][1] 可能非常小，导致下一步大
        pre[shelf_width - books[0][0]] = [books[0][1], books[0][1]]
        for i in range(1, len(books)):
            next = {}
            search = sorted(list(pre.keys()))[::-1]
            h = float('inf')
            for j in range(len(search)):
                if pre[search[j]][0] < h:
                    h = pre[search[j]][0]
                    if books[i][0] <= search[j]:
                        if search[j] - books[i][0] not in next:
                            next[search[j] - books[i][0]] = [
                                pre[search[j]][0] + max(0, books[i][1] - pre[search[j]][1]),
                                max(books[i][1], pre[search[j]][1])]
                        else:
                            if pre[search[j]][0] + max(0, books[i][1] - pre[search[j]][1]) < \
                                    next[search[j] - books[i][0]][0]:
                                next[search[j] - books[i][0]] = [
                                    pre[search[j]][0] + max(0, books[i][1] - pre[search[j]][1]),
                                    max(books[i][1], pre[search[j]][1])]
            next[shelf_width - books[i][0]] = [h + books[i][1], books[i][1]]
            pre = next
        res = float('inf')
        for val in pre.values():
            if val[0] < res:
                res = val[0]
        return res

    def minHeightShelves(self, books: list, shelf_width: int) -> int:
        dp = [float('inf') for _ in range(len(books) + 1)]
        dp[0] = 0
        for i in range(1,len(dp)):
            max_width = shelf_width
            max_height = 0
            j = i - 1
            while j >= 0 and max_width >= books[j][0]:
                max_width -= books[j][0]
                max_height = max(max_height,books[j][1])
                dp[i] = min(dp[i],dp[j] + max_height)
                j -= 1

        return dp[-1]

    def parseBoolExpr(self, expression: str) -> bool:

        def sub_search(exp):
            if '(' not in exp[2:]:
                if exp[0] == '!':
                    if 't' not in exp:
                        return 't'
                    else:
                        return 'f'
                elif exp[0] == '&':
                    if 'f' not in exp:
                        return 't'
                    else:
                        return 'f'
                elif exp[0] == '|':
                    if 't' not in exp:
                        return 'f'
                    else:
                        return 't'
            else:
                next = ''
                i = 0
                visit = exp[2:-1]
                while i < len(visit):
                    if visit[i] in ['!','&','|']:
                        j = i + 2
                        count = 1
                        cur = visit[i] + '('
                        while count != 0:
                            if visit[j] == '(':
                                count += 1
                            elif visit[j] == ')':
                                count -= 1
                            cur += visit[j]
                            j += 1
                        next += sub_search(cur)
                        i = j
                    else:
                        next += visit[i]
                        i += 1
                return sub_search(exp[:2] + next + exp[-1])

        res = sub_search(expression)
        if res == 't':
            return True
        else:
            return False


A = Solution()
print(A.parseBoolExpr("!(f)"))
