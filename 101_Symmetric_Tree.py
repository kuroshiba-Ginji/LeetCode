# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:

    def check(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        a = self.check(left.left, right.right) #再起的に左ノードの左の葉の値と右ノードの右葉の値が一致しているかを確認
        b = self.check(left.right, right.left)　#再起的に左ノードの右の葉の値と右ノードの左葉の値が一致しているかを確認
        return a and b


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.check(root.left, root.right)
