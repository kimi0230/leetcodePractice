# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def insert(self, data):
        # Compare the new value with the parent node
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    # 前序走訪
    def preOrder(self):
        if self == None:
            return
        print(self.val)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 節點為null或沒有子節點，不用反轉，終止遞迴
        if root == None or (root.right == None and root.left == None):
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

if __name__ == '__main__':
    sol = Solution()
    test_object = TreeNode(10)
    test_object.insert(8)
    test_object.insert(20)
    test_object.insert(15)
    test_object.insert(9)
    test_object.insert(7)
    print(test_object.preOrder())
    print('---')
    print(sol.invertTree(test_object).preOrder())


#      10
#     /  \
#    8    20
#   / \   /
#  7   9 15

#      10
#     /  \
#    20    8
#   / \   / \
#     15 9  7

# 10 8 7 9 20 15 None

# 10 20 15 8 9 7 None
