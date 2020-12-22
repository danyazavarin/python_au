# Tree

## Validate Binary Search Tree

+ [Validate Binary Search Tree](#validate-binary-search-tree)

https://leetcode.com/problems/validate-binary-search-tree/

``` python
def isValidBST(self, root: TreeNode) -> bool:
    def is_in_range(node=root, range_start=-inf, range_end=inf):
        if not node:
            return True
        if node.val <= range_start or node.val >= range_end:
            return False
        return is_in_range(node.left, range_start, node.val) and is_in_range(node.right, node.val, range_end)
    return is_in_range()
```