class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        ret = 0
        if root is not None and root.val is not None:
            if root.val == sum:
                ret += 1
            ret += self.dfs(root.left, sum, root.val)
            ret += self.dfs(root.right, sum, root.val)
            ret += self.pathSum(root.left, sum)
            ret += self.pathSum(root.right, sum)
        return ret

    def dfs(self, root: TreeNode, target: int, current: int) -> int:
        ret = 0
        
        if root is not None and root.val is not None:
            if current + root.val == target:
                ret += 1
            ret += self.dfs(root.left, target, current + root.val)
            ret += self.dfs(root.right, target, current + root.val)
        return ret
