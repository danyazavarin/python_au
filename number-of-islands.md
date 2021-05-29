# graph

+ [Course Schedule II](#course-schedule-II)
+ [Course Schedule](#course-schedule)
+ [Number of Islands](#number-of-islands)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
from collections import deque
def dfs(self, curr, visited, adj_list, answer):
    visited[curr] = 1 
    for neighbor in adj_list[curr]:
        if neighbor not in visited:
            if self.dfs(neighbor, visited, adj_list, answer):
                return True
        elif visited[neighbor] == 1:
            return True
    visited[curr] = 2
    answer.appendleft(curr)
    return False
    

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj_list = [[] for i in range(numCourses)]
    for course, pre in prerequisites:
        adj_list[pre].append(course)
    visited = {}
    answer = deque()
    for curr in range(numCourses):
        if curr not in visited:
            if self.dfs(curr, visited, adj_list, answer):
                return []
    return answer
```


## Course Schedule

https://leetcode.com/problems/course-schedule/

```python
from collections import deque
def dfs(self, curr, visited, adj_list, answer):
    visited[curr] = 1 
    for neighbor in adj_list[curr]:
        if neighbor not in visited:
            if self.dfs(neighbor, visited, adj_list, answer):
                return True
        elif visited[neighbor] == 1:
            return True
    visited[curr] = 2
    answer.appendleft(curr)
    return False
    

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj_list = [[] for i in range(numCourses)]
    for course, pre in prerequisites:
        adj_list[pre].append(course)
    visited = {}
    answer = deque()
    for curr in range(numCourses):
        if curr not in visited:
            if self.dfs(curr, visited, adj_list, answer):
                return []
    if answer == []:
        return 0
    else:
        return 1
```


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
