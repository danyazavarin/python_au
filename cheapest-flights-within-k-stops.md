# Graph

+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

``` python
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

    if src == dst: return 0
    d = collections.defaultdict(list)
    seen =  collections.defaultdict(lambda: float('inf'))
    for u, v, p in flights:
        d[u] += [(v, p)]

    q = [(src, -1, 0)]

    while q:
        pos, k, cost = q.pop(0)
        if pos == dst or k == K: continue
        for nei, p in d[pos]:
            if cost + p >= seen[nei]:
                continue
            else:
                seen[nei] = cost+p
                q += [(nei, k+1, cost+p)]

    return seen[dst] if seen[dst] < float('inf') else -1
```
