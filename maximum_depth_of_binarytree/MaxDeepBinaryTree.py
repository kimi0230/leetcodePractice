# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# 找出一個二元樹的深度

# Definition for a binary tree node.


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

    # 中序走訪
    def inOrder(self):
        if self == None:
            return
        if self.left:
            self.left.inOrder()
        print(self.val)
        if self.right:
            self.right.inOrder()

    # 後序走訪
    def postOrder(self):
        if self == None:
            return
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.val)


class Solution(object):
    # 節點如果left或right有值，則depth+1，並判斷left或right有沒有子節點 到最底層
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0

        l_depth = 1
        r_depth = 1

        if root.left:
            l_depth += self.maxDepth(root.left)
            # self.maxDepth(root.left)
        if root.right:
            r_depth += self.maxDepth(root.right)
            # self.maxDepth(root.right)
        return max(l_depth, r_depth)

    def maxDepth_one_line(self, root):
        # return root and 1 + max(map(self.maxDepth, (root.left, root.right))) or 0
        return 1 + max(map(self.maxDepth_one_line, (root.left, root.right))) if root else 0


if __name__ == '__main__':
    sol = Solution()
    # [3, 9, 20, null, null, 15, 7]
    #     3
    #    / \
    #       9
    #      /  \
    #     7    20
    #          /
    #        15
    test_object = TreeNode(3)
    test_object.insert(9)
    test_object.insert(20)
    test_object.insert(15)
    test_object.insert(7)
    # test_object.inOrder()

    print(sol.maxDepth(test_object))

#    map() 會根據提供的函數對指定的序列做映射
#    第一個參數  每一個元素調用 function 函数
#    返回包含每次function函數版回值的新列表
# def square(x):
#     return x ** 2
# map(square, [1, 2, 3, 4, 5])   # 結果 [1, 4, 9, 16, 25]
