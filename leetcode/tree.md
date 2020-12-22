# Tree

## Kth Smallest Element in a BST

+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

``` python
def do(self, cur, nodes):
    if cur is None:
        return 0
    self.do(cur.left, nodes)
    nodes.append(cur.val)
    self.do(cur.right, nodes)

def kthSmallest(self, root: TreeNode, k: int) -> int:
    nodes = []
    self.do(root, nodes)
    return nodes[k-1]
```