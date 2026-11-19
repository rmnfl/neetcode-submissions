# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        return self._mergeKLists(lists, 0, len(lists) - 1)

    def _mergeKLists(self, lists, s, e):
        if s == e:
            return lists[s]
        if s > e:
            return None

        m = (s + e) // 2

        left = self._mergeKLists(lists, s, m)
        right = self._mergeKLists(lists, m + 1, e)

        return self._merge2Lists(left, right)

    def _merge2Lists(self, head1, head2):
        head = curr = ListNode(-1)

        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next

        while head1:
            curr.next = head1
            head1 = head1.next
            curr = curr.next
        while head2:
            curr.next = head2
            head2 = head2.next
            curr = curr.next

        return head.next
