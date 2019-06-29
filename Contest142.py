class MountainArray:
    def __init__(self,arr):
        self.arr = arr
        self.count = 0

    def get(self, index: int) -> int:
        self.count += 1
        #print(self.count)
        return self.arr[index]
    def length(self) -> int:
        self.count += 1
        #print(self.count)
        return len(self.arr)

class Solution:
    def sampleStats(self, count: list) -> list:
        total = 0
        total_v = 0
        max_v = 0
        min_v = -1
        mode = 0
        for i in range(len(count)):
            if min_v == -1 and count[i] != 0:
                min_v = i
            if count[i] != 0:
                max_v = i
                total += count[i]
                total_v += count[i] * i
                if count[i] > count[mode]:
                    mode = i
        mean = total_v / total
        cur = 0
        median_list = []
        for i in range(len(count)):
            cur += count[i]
            if total % 2 == 1:
                if cur > total // 2:
                    median_list.append(i)
                    break
            if total % 2 == 0:
                if cur == total // 2:
                    median_list.append(i)
                elif cur > total // 2:
                    median_list.append(i)
                    break
        median = sum(median_list) / len(median_list)
        return [float(min_v),float(max_v),float(mean),float(median),float(mode)]

    def carPooling(self, trips: list, capacity: int) -> bool:
        memo = [0 for _ in range(1000)]
        for i in range(len(trips)):
            for j in range(trips[i][1], trips[i][2]):
                memo[j] += trips[i][0]
                if memo[j] > capacity:
                    return False
        return True

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        left = 0
        right = N - 1
        while left < right:
            middle = (left + right) // 2
            if mountain_arr.get(middle) < mountain_arr.get(middle + 1):
                left = middle + 1
            else:
                right = middle
        peak = left
        # up search
        left = 0
        right = peak
        #print(peak)
        while left < right:
            middle = (left + right) // 2
            cur = mountain_arr.get(middle)
            if target == cur:
                return middle
            elif target > cur:
                left = middle + 1
            else:
                right = middle
        left = peak
        right = N
        while left < right:
            middle = (left + right) // 2
            cur = mountain_arr.get(middle)
            if target == cur:
                return middle
            elif target < cur:
                left = middle+1
            else:
                right = middle
        return -1

    def braceExpansionII(self, expression: str) -> list:

        def divide(sub):
            print(sub,'!')
            if ',' not in sub and '{' not in sub:
                return {sub}
            if not sub:
                return set()
            memo = []
            oper = []
            cur = ''
            count = 0
            pre = ''
            for s in sub:
                if s == ',':
                    if count == 0 and cur:
                            memo.append(cur)
                            oper.append('+')
                            cur = ''
                    else:
                        cur += s
                elif s == '{':
                    if cur and count == 0:
                        memo.append(cur)
                        oper.append('*')
                        cur = ''
                    cur += '{'
                    count += 1
                elif s == '}':
                    count -= 1
                    cur += '}'
                else:
                    if count == 0 and cur and pre == '}':
                        memo.append(cur)
                        oper.append('*')
                        cur = ''
                    cur += s
                pre = s
            if cur:
                memo.append(cur)

            if len(memo) == 1:
                return divide(memo[0][1:-1])
            for i in range(len(memo)):
                memo[i] = divide(memo[i])

            return product(memo,oper)


        def product(memo,oper):
            if len(oper) == len(memo):
                oper = oper[:-1]
            print(memo,oper,'^')
            cur = set()
            new_memo = []
            for i in range(len(oper)):
                if oper[i] == '+':
                    new_memo.append(memo[i])
                else:
                    next = set()
                    cur_l = list(memo[i])
                    cur_memo= list(memo[i+1])
                    for j in range(len(cur_l)):
                        for k in range(len(cur_memo)):
                            next.add(cur_l[j] + cur_memo[k])
                    memo[i+1] = next
                    print(next,'[')

            new_memo.append(memo[-1])
            print(new_memo,'%')
            for i in range(len(new_memo)):
                cur |= new_memo[i]
            print(cur,'$')
            return cur

        return sorted(list(divide(expression)))

A = Solution()

print(A.braceExpansionII('{a}{a}{a}'))