# Math

## Base 7

+ [Base 7](#base-7)

https://leetcode.com/problems/base-7/

``` python
def convertToBase7(self, num: int) -> str:
    if not num: return '0'
    l, n = [], num < 0
    if n:
        num *= -1
    while num:
        l.append(str(num % 7))
        num //= 7
    if n:
        l.append('-')
    return ''.join(l[::-1])
```