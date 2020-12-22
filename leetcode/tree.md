# Tree

## Symmetric Tree

+ [Symmetric Tree](#symmetric-tree)

https://leetcode.com/problems/symmetric-tree/

``` python
def isSymmetric(self, root: TreeNode) -> bool:
    def symm(elem1, elem2):
        if elem1 == None and elem2 == None:
            return True
        if (elem1 == None and elem2 != None) or (elem2 == None and elem1 != None):
            return False
        return elem1.val == elem2.val and symm(elem1.left, elem2.right) and symm(elem1.right, elem2.left)
    return symm(root, root)
```