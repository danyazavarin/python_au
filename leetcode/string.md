# String

## Reverse Words in a String III

+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)

https://leetcode.com/problems/reverse-words-in-a-string-iii/

``` python
def reverseWords(self, s: str) -> str:
    return " ".join([i[::-1] for i in s.split()])
```