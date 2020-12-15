# String

## Reverse String

+ [Reverse String](#reverse-string)

https://leetcode.com/problems/reverse-string/

``` python
def reverseString(self, s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
```