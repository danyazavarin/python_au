# Linked-list

## Linked List Cycle

+ [Linked List Cycle](#linked-list-cycle)

https://leetcode.com/problems/linked-list-cycle/

``` python
def hasCycle(self, head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
```