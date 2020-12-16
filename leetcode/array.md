# Array

## Image Smoother

+ [Image Smoother](#image-smoother)

https://leetcode.com/problems/image-smoother/

``` python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    m, n = len(M), len(M[0])
    A = [[0]*n for i in range(m)]
    for i,j in product(range(m), range(n)):
        s = []
        for I,J in product(range(max(0,i-1),min(i+2,m)),range(max(0,j-1),min(j+2,n))):
            s.append(M[I][J])
        A[i][j] = int(sum(s)/len(s))
    return A
```