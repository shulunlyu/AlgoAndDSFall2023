from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Question1 Minimum Depth of Binary Tree

    def minDepth(self, root: Optional[TreeNode]):
        if not root:
            return 0
        l,r = self.minDepth(root.left),self.minDepth(root.right)
        if not root.left:
            return 1+r
        if not root.right:
            return 1+l
        return 1+min(l,r)

    # Question2 Count Complete Tree Nodes

    def countNodes(self, root: Optional[TreeNode]):
        def getLeftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        def getRightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
        if not root: return 0

        L,R = getLeftHeight(root), getRightHeight(root)
        if L == R:
            return 2**L - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Question3 Find Largest Value in Each Tree Row
    
    def largestValues(self, root: Optional[TreeNode]):
        if not root: return []
        res = []
        q = [root]
        while q:
            new_q = []
            maxV = -float('inf')
            for curr in q:
                maxV = max(maxV,curr.val)
                if curr.left:
                    new_q.append(curr.left)                 
                if curr.right:
                    new_q.append(curr.right)
            res.append(maxV)
            q = new_q
        return res

    # Question4 Leaf-Similar Tree

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root1) == dfs(root2)

    # Question5 Deepest Leaves Sum

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                level.append(curr.val)
            res.append(level)
        return sum(res[-1])