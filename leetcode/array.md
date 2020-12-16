# Array

## Max Consecutive Ones

+ [Max Consecutive Ones](#max-consecutive-ones)

https://leetcode.com/problems/max-consecutive-ones/

``` python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    return max(list(map(len, ("".join(list(map(str, nums)))).split('0'))))
```