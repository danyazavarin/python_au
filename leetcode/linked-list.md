# Linked-list

## Remove Nth Node From End of List

+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

``` python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    fast=slow=head
    for i in range(n):
        fast=fast.next
    if not fast:
        return head.next
    while fast.next:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return head
```