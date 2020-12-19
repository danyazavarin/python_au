# Linked-list

## Sort List

+ [Sort List](#sort-list)

https://leetcode.com/problems/sort-list/

``` python
def sortList(self, head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    p, slow, fast = None, head, head
    while fast and fast.next:
        p = slow
        slow = slow.next
        fast = fast.next.next
    p.next = None
    return self.merge(self.sortList(head), self.sortList(slow))
def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
    cur = output = ListNode()
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1 == None:
        cur.next = l2
    if l2 == None:
        cur.next = l1
    return output.next
```