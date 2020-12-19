# Linked-list

## Linked List Cycle II

+ [Linked List Cycle II](#linked-list-cycle-ii)

https://leetcode.com/problems/linked-list-cycle-ii/

``` python
def detectCycle(self, head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
```