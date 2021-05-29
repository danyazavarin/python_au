# Graph

+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

``` python
def maxDepth(self, root: 'Node') -> int:
    queue = []
    if root: queue.append((root,1))
    depth = 0
    for (node, level) in queue:
        depth = level
        queue += [(child, level+1) for child in node.children]
    return depth
```
