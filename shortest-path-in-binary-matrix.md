# Graph

+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    if grid[0][0] == 1:
        return -1
    m = [(0, 0, 1)]
    while len(m) > 0:
        x, y, z = m.pop(0)
        if x == rows - 1 and y == cols - 1:
            return z
        arr = [(x+1, y), (x, y-1), (x, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1), (x+1, y+1), (x-1, y)]
        for a, b in arr:
            if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 0:
                grid[a][b] = 1
                m.append((a, b, z + 1))
    return -1
```
