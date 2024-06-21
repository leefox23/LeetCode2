# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfsInorder(self, root):
        if root is None: return
        self.dfsInorder(root.left)
        self.represented.append(root.val)
        self.dfsInorder(root.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.represented = []
        self.dfsInorder(root)

        pointer = answer = TreeNode(self.represented[0])
        for node in self.represented[1:]:
            pointer.right = TreeNode(node)
            pointer = pointer.right

        return answer