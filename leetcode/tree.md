# Tree

## Binary Tree Level Order Traversal

+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)

https://leetcode.com/problems/binary-tree-level-order-traversal/

``` python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
        return
    out = []
    q = [root]
    while q:
        level = len(q)
        ans = []
        while level:
            node = q.pop(0)
            level -=1
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(ans)
    return out
```