# Math

## Largest Perimeter Triangle

+ [Largest Perimeter Triangle](#largest-perimeter-triangle)

https://leetcode.com/problems/largest-perimeter-triangle/

``` python
def largestPerimeter(self, A: List[int]) -> int:
    A.sort( reverse = True )
    for i in range( len(A) - 2):
        if A[i] < A[i+1] + A[i+2]:
            return A[i] + A[i+1] + A[i+2]
    return 0
```