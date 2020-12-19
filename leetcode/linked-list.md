# Linked-list

## Middle of the Linked List

+ [Middle of the Linked List](#middle-of-the-linked-list)

https://leetcode.com/problems/middle-of-the-linked-list/

``` python
def middleNode(self, head: ListNode) -> ListNode:
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow
```