# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getValue(self, root, res):
        if root:
            self.getValue(root.left, res) #再起的に左側の値を追加する
            res.append(root.val) #親ノードの値を追加する
            self.getValue(root.right, res) #右再起的に側のノードの値を追加する

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.getValue(root, res)
        return res
