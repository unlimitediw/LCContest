# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.newStack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.newStack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.newStack.pop(-1)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.newStack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.newStack


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return
        right = root.left
        root.left = root.right
        root.right = right
        self.dfs(root.left)
        self.dfs(root.right)

    def invertTree2(self, root):
        if root:
            root.left, root.right = self.invertTree2(root.right), self.invertTree2(root.left)
        return root

    def calculate(self, s):
        self.s = s
        return self.calculateIter(0, 1)

    def calculateIter(self, start, sign):
        """
        :type s: str
        :rtype: int
        """
        while self.s[start] == ' ':
            start += 1
        now = int(self.s[start])
        k = start
        while k + 1 < len(self.s):
            if 47 < ord(self.s[k + 1]) < 58:
                now = now * 10 + int(self.s[k + 1])
                k += 1
            elif self.s[k + 1] == ' ':
                k += 1
            else:
                break

        for i in range(k + 1, len(self.s)):
            if self.s[i] == ' ':
                continue
            if self.s[i] == '+':
                return sign * now + self.calculateIter(i+1, 1)
            elif self.s[i] == '-':
                return sign * now + self.calculateIter(i+1, -1)
            elif self.s[i] == '*':
                next = 0
                while i + 1 < len(self.s):
                    if 47 < ord(self.s[i + 1]) < 58:
                        next = next * 10 + int(self.s[i + 1])
                        i += 1
                    elif self.s[i + 1] == ' ':
                        i += 1
                    else:
                        break
                now *= next
            elif self.s[i] == '/':
                next = 0
                while i + 1 < len(self.s):
                    if 47 < ord(self.s[i + 1]) < 58:
                        next = next * 10 + int(self.s[i + 1])
                        i += 1
                    elif self.s[i + 1] == ' ':
                        i += 1
                    else:
                        break
                now = now // next
        return sign*now

def calculate2(self, s):
    if not s:
        return "0"
    stack, num, sign = [], 0, "+"
    for i in range(len(s)):
        if s[i].isdigit():
            num = num*10+ord(s[i])-ord("0")
        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
            if sign == "-":
                stack.append(-num)
            elif sign == "+":
                stack.append(num)
            elif sign == "*":
                stack.append(stack.pop()*num)
            else:
                tmp = stack.pop()
                if tmp//num < 0 and tmp%num != 0:
                    stack.append(tmp//num+1)
                else:
                    stack.append(tmp//num)
            sign = s[i]
            num = 0
    return sum(stack)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

print(Solution().calculate('3+2*2'))
