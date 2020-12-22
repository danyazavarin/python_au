# Tree

## Binary Tree Inorder Traversal

+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)

https://leetcode.com/problems/binary-tree-inorder-traversal/

``` python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    self.traverse(root, res)
    return res


def traverse(self, node,order):
    if node is None:
        return
    self.traverse(node.left, order)
    order.append(node.val)
    if node is None:
        return
    self.traverse(node.right, order)
```