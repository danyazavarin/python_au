# Linked-list

## Merge Two Sorted Lists

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

https://leetcode.com/problems/merge-two-sorted-lists/

``` python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    pointer = head = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            pointer.next = l1
            l1 = l1.next
        else:
            pointer.next = l2
            l2 = l2.next
        pointer = pointer.next
    pointer.next = l1 if l1 else l2
    return head.next
```