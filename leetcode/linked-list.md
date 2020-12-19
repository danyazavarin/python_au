# Linked-list

## Reorder List

+ [Reorder List](#reorder-list)

https://leetcode.com/problems/reorder-list/

``` python
def Reverse(self, head):
    prev = None
    cur = head
    while cur:
        next_pointer = cur.next
        cur.next = prev
        prev = cur
        cur = next_pointer
    return prev

def reorderList(self, head: ListNode) -> None:
    if not head:
        return head
    slow=fast=head0=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    reverse=self.Reverse(slow.next)
    slow.next=None
    lst=ListNode()
    while reverse:
        lst=head0.next
        head0.next=reverse
        head0=reverse
        reverse=lst
```