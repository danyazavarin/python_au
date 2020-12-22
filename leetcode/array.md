# Array

## Reshape the Matrix

+ [Reshape the Matrix](#reshape-the-matrix)

https://leetcode.com/problems/reshape-the-matrix/

``` python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    if len(nums)*len(nums[0])!=r*c:
        return nums
    mat=[]
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            mat.append(nums[i][j])
    res=[]
    for i in range(0,len(mat),c):
        res.append(mat[i:i+c])
    return res
```