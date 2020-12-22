# Array

## Squares of a Sorted Array

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

https://leetcode.com/problems/squares-of-a-sorted-array/

``` python
def sortedSquares(self, nums: List[int]) -> List[int]:
    nums=[x*x for x in nums]
    return sorted(nums)
```