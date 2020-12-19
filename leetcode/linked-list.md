# Linked-list

## Reverse Linked List

+ [Reverse Linked List](#reverse-linked-list)

https://leetcode.com/problems/reverse-linked-list/

``` python
def sortedSquares(self, nums: List[int]) -> List[int]:
    prev = None
    next = None
    cur = head
    while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return  prev
```