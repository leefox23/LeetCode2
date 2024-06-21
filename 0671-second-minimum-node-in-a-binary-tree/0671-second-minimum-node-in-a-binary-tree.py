# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def solve(node: Optional[TreeNode], values: Set[int]) -> None:
            if node:
                values.add(node.val)
                solve(node.left, values)
                solve(node.right, values)
        
        values = set()
        solve(root, values)

        min_value = min(values)
        values.remove(min_value)

        return min(values) if values else -1