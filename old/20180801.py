# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myQueue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.myQueue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.myQueue.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.myQueue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.myQueue:
            return True
        else:
            return False

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 找出权重最大的两个数(>3/N) O(1)space linear time
        # 3/n很特殊的，1：1：1
        # 两个记分牌一起往后走，遇到都不同就减，为0时更换牌子的id，最后得到的牌子肯定时当中最大的两个数，或者不是最大的两个，但是同时也证明了前面最大的数也无法超过1/3N（重点是如果前面有个数抵消太多C1C2的并不在后面出现的话？这三个数的和并不允许第四个3/N数出现了）

        num1 = None
        num2 = None
        count1 = 0
        count2 = 0

        for i in range(len(nums)):
            if num1 == nums[i]:
                count1 += 1
            elif num2 == nums[i]:
                count2 += 1
            elif count1 == 0:
                num1 = nums[i]
                count1 = 1
            elif count2 == 0:
                num2 = nums[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1

        res = []
        if count1 > len(nums)/3:
            res.append(num1)
        if count2 > len(nums)/3:
            res.append(num2)

        return res

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.count = 0
        self.k = k
        self.res = None
        self.findMinKth(root)
        return self.res

    def findMinKth(self,root):
        if not root:
            return
        self.findMinKth(root.left)
        self.count += 1
        if self.count == self.k:
            self.res = root.val
        self.findMinKth(root.right)

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                return False
        return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        fakerList = [head.val]
        while head.next:
            head = head.next
            fakerList.append(head.val)
        return fakerList == fakerList[::-1]

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


























print(Solution().majorityElement([8,8,7,7,7]))
