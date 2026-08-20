# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left

#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level=0
        res=[]
        queue=deque([root])
        while queue:
            current=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                current.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level%2==1:
                current.reverse()
            level+=1
            res.append(current)
        return res
            
            