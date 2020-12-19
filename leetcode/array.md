# Array

## Transpose Matrix

+ [Transpose Matrix](#transpose-matrix)

https://leetcode.com/problems/transpose-matrix/

``` python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    return [list(i) for i in zip(*A)]
```