# Intervals

## Insert Interval

+ [Insert Interval](#insert-interval)

https://leetcode.com/problems/insert-interval/

``` python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    i = 0
    intervals = sorted(intervals)
    while i < len(intervals) and intervals[i][0] < newInterval[0]:
       i+=1
    intervals.insert(i,newInterval)
    merge = []
    for i in intervals:
        if not merge or merge[-1][1] < i[0]:
            merge.append(i)
        else:
            merge[-1][1] = max(merge[-1][1],i[1])
    return merge
```