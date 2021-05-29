# Graph

+ [Course Schedule](#course-schedule)

## Course Schedule
 
https://leetcode.com/problems/course-schedule/

``` python
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    count = 0
    todo = {i: set() for i in range(numCourses)}
    outdegree = [[] for _ in range(numCourses)]
    for i in prerequisites:
        todo[i[0]].add(i[1])
        outdegree[i[1]].append(i[0])
    start = [i for i in range(numCourses) if not todo[i]]
    while start:
        newStart = []
        for i in start:
            count += 1
            for j in outdegree[i]:
                todo[j].remove(i)
                if not todo[j]:
                    newStart.append(j)
        start = newStart
    return count == numCourses
```
