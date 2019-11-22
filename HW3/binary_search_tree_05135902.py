class TreeNode(object):
    """
    :type val: int
    :type left: TreeNode or None
    :type right: TreeNode or None
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root = TreeNode(val)
        elif val == root.val:
            nn = TreeNode(val)
            nn.left = root.left
            root.left = nn
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def findMin(self, root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root

    def delete(self, root, val):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if root == None:
            return
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.left and root.right:
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.delete(root.right, temp.val)
            elif root.right == None and root.left == None:
                root = None
            elif root.right == None:  # delete all the same numbers in left child.
                root = self.delete(root.left,val)
            elif root.left == None:
                root = root.right
        return root

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root == None:
            return root
        if root.val == target:
            return root
        elif target < root.val:
            return self.search(root.left, target)
        elif target > root.val:
            return self.search(root.right, target)

    def count(self, root, val):
        if root == None:
            return 0
        if root.val == val:
            return 1 + self.count(root.left, val)
        if val < root.val:
            return self.count(root.left, val)
        if val > root.val:
            return self.count(root.right, val)

    def getDepth(self, root):
        depth = 0
        if root == None:
            return depth
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        return max(left, right) + 1

    def helper(self, A, s, e):
        root = None
        if s < e:
            mid = (s + e) >> 1
            root = TreeNode(A[mid])
            root.left = self.helper(A, s, mid - 1)
            root.right = self.helper(A, mid + 1, e)
        elif s == e:
            root = TreeNode(A[s])
        return root

    def sortList(self, root):
        rtn = []
        if root == None:
            return rtn
        a = self.sortList(root.left)
        b = self.sortList(root.right)
        return a + [root.val] + b


    def modify(self, root, val, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """
        cnt = self.count(root, val)
        oldDepth = self.getDepth(root)

        node = self.delete(root, val)
        while node and cnt:
            self.insert(node, new_val)
            cnt -= 1
        newDepth = self.getDepth(node)
        if newDepth > oldDepth:
            lst = self.sortList(node)
            if lst is None or len(lst) == 0:
                return None
            res = self.helper(lst, 0, len(lst) - 1)
            return res
        else:
            return node

    def printTree(self, root, order='pre'):
        if root == None:
            return
        if order == 'pre':
            print(root.val, end = ' ')
            self.printTree(root.left)
            self.printTree(root.right)
        elif order == 'in':
            self.printTree(root.left)
            print(root.val, end = ' ')
            self.printTree(root.right)
        elif order == 'post':
            self.printTree(root.left)
            self.printTree(root.right)
            print(root.val, end = ' ')
