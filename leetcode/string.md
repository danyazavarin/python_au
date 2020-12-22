# String

## Valid Anagram

+ [Valid Anagram](#valid-anagram)

https://leetcode.com/problems/valid-anagram/

``` python
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```