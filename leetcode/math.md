# Math

## Palindrome Number

+ [Palindrome Number](#palindrome-number)

https://leetcode.com/problems/palindrome-number/

``` python
def isPalindrome(self, x: int) -> bool:
    if (x < 0) or ((x % 10 == 0) and (x != 0)):
        return 0
    rnum = 0
    t = x
    while(t > 0):
        rnum = rnum * 10 + t % 10
        t //= 10
    return x == rnum
```