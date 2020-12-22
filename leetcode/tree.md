# Tree

## Binary Search Tree Iterator

+ [Binary Search Tree Iterator](#binary-search-tree-iterator)

https://leetcode.com/problems/binary-search-tree-iterator/

``` python
def __init__(self, root: TreeNode):
    self.nodes_sorted = []
    self.index = -1
    self._inorder(root)

def _inorder(self, root):
    if not root:
        return
    self._inorder(root.left)
    self.nodes_sorted.append(root.val)
    self._inorder(root.right)

def next(self) -> int:
    self.index += 1
    return self.nodes_sorted[self.index]

def hasNext(self) -> bool:
    return self.index + 1 < len(self.nodes_sorted)
```