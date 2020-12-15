# Math

## Fibonacci Number

+ [Fibonacci Number](#fibonacci-number)

https://leetcode.com/problems/fibonacci-number/

``` python
def fib(self, n: int) -> int:
    first = 0
    second = 1
    sum_f_s = 0
    count = 1
    if n == 0 or n == 1:
        return n
    while(count < n):
        sum_f_s = first + second
        first,second = second,sum_f_s
        count += 1
    return sum_f_s
```