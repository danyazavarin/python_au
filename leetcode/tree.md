# Tree

## Maximum Depth of Binary Tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)

https://leetcode.com/problems/maximum-depth-of-binary-tree/

``` python
def maxDepth(self, root: TreeNode) -> int:
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
```