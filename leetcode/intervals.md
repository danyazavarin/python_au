# Intervals

## Non-overlapping Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)

https://leetcode.com/problems/non-overlapping-intervals/

``` python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals = sorted(intervals)
    prev = float("-inf")
    count = 0
    for i in intervals:
        if i[0] >= prev:
            prev = i[1]
        else:
            count +=1
            prev = min(prev,i[1])
    return count
```