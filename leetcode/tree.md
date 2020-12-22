# Tree

## Invert Binary Tree

+ [Invert Binary Tree](#invert-binary-tree)

https://leetcode.com/problems/invert-binary-tree/

``` python
def invertTree(self, root: TreeNode) -> TreeNode:
    if root is None:
        return
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
```