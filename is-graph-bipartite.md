+ [Is Graph Bipartite?](#is-graph-bipartite?)

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

```python
def isBipartite(self, graph):
    blank = 0
    red = 1
    green = 2
    n = len(graph)
    visited = [blank]*n
    print(visited)
    for i in range(n):
        if not visited[i]:
            que = deque([i])
            visited[i] = red
            while que:
                i = que.popleft()
                for j in graph[i]:
                    if visited[i] == visited[j]:
                        return False
                    if not visited[j]:
                        visited[j] = 3 - visited[i]
                        que.append(j)
    return True
```
