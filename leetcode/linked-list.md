# Linked-list

## Palindrome Linked List

+ [Palindrome Linked List](#palindrome-linked-list)

https://leetcode.com/problems/palindrome-linked-list/

``` python
def isPalindrome(self, head: ListNode) -> bool:
    lst = []
    while(head):
        lst.append(head.val)
        head = head.next
    p1 = 0
    p2 = len(lst)-1
    while(p1<p2):
        if lst[p1]!=lst[p2]:
            return False
        else:
            p1+=1
            p2-=1
    return True
```