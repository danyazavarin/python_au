# graph

+ [Number of Islands](#number-of-islands)

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
def dfs(self, grid, row, col, n):
    if  0 <= row < len(grid) and 0 <= col < n and grid[row][col] == "1":
        grid[row][col] = "0"
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.dfs(grid, row + x , col + y, n)
        
def numIslands(self, grid: List[List[str]]) -> int:
    counter = 0
    m = len(grid)
    n = len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == '1':
                self.dfs(grid, row, col, n)
                counter += 1
    return counter 
```
