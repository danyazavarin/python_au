# Linked-list

## Intersection of Two Linked Lists

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

https://leetcode.com/problems/intersection-of-two-linked-lists/

``` python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if headA == None or headB == None:
        return None
    A_pointer = headA
    B_pointer = headB
    while A_pointer != B_pointer:
        A_pointer = headB if A_pointer == None else A_pointer.next
        B_pointer = headA if B_pointer == None else B_pointer.next
    return A_pointer
```