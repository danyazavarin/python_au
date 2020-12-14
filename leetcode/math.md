# Math

## Reverse Integer

+ [Reverse Integer](#reverse-integer)

https://leetcode.com/problems/reverse-integer/

``` python
def reverse(self, x: int) -> int:
    a = 0
    if x == 0:
        return x
    elif x < 0:
        x = x * (-1)
        while x != 0:
            a = a * 10 + x % 10
            x = x // 10
        if abs(a) < pow(2,31) - 1:
            return a * (-1)
        else:
            return 0
    else:
        while x != 0:
            a = a * 10 + x % 10
            x = x // 10
        if abs(a) < pow(2,31) - 1:
            return a
        else:
            return 0
```