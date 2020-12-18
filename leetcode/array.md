# Array

## Flipping an Image

+ [Flipping an Image](#flipping-an-image)

https://leetcode.com/problems/flipping-an-image/

``` python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    for r in range(len(A)):
        row=A[r]
        A[r]=row[::-1]

    for r in range(len(A)):
        for c in range(len(A[0])):
            A[r][c]=0 if A[r][c]==1 else 1
    return A
```