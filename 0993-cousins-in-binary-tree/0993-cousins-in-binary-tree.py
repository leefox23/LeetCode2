# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(root, None)]

        while queue:
            newQueue = []

            xParent = None
            yParent = None

            for node, parent in queue:
                if node.val == x:
                    xParent = parent
                elif node.val == y:
                    yParent = parent

                if xParent and yParent:
                    return xParent != yParent

                if node.left:
                    newQueue.append((node.left, node))
                if node.right:
                    newQueue.append((node.right, node))

            queue = newQueue

        return False