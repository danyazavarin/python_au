# Dynamic Progamming

+ [House Robber](#house-robber)

## House Robber

https://leetcode.com/problems/house-robber/ 

```python
def rob(self, nums: List[int]) -> int:
    rob1, rob2 = 0, 0
    for num in nums:
        newrob = max(rob1+num, rob2)
        rob1 = rob2
        rob2 = newrob
    return rob2
```
