# Array

## Move Zeroes

+ [Move Zeroes](#move-zeroes)

https://leetcode.com/problems/move-zeroes/

``` python
def moveZeroes(self, nums: List[int]) -> None:
    z = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[z]=nums[i]
            z+=1
    for k in range(z,len(nums)):
        nums[k]=0
```