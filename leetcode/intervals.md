# Intervals

## Non-overlapping Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)

https://leetcode.com/problems/non-overlapping-intervals/

``` python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x:x[1])
    prev = float("-inf")
    ans = 0
    for i in intervals:
        if i[0] >= prev:
            prev = i[1]
        else:
            ans += 1
    return ans
```