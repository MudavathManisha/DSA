# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0
        def cal_height(node):
            if not node:
                return 0
            left_height=cal_height(node.left)
            right_height=cal_height(node.right)
            self.max_diameter=max(self.max_diameter,left_height+right_height)
            return 1+max(left_height,right_height)
        cal_height(root)
        return self.max_diameter

        