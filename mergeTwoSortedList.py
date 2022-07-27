
from typing import List, Optional
from ListNode import ListNode

def construct(lis: List[int]) -> ListNode:
    dummy = ListNode()
    pointer = dummy
    for i in range(len(lis)):
        pointer.next = ListNode(lis[i])
        pointer = pointer.next
    return dummy.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        i = list1
        j = list2
        k = dummy
        
        while i is not None and j is not None:
            if i.val <= j.val:
                k.next = i
                i = i.next
            else:
                k.next = j
                j = j.next
                
            k = k.next
        
        while i is not None:
            k.next = i
            i = i.next
            k = k.next

        while j is not None:
            k.next = j
            j = j.next
            k = k.next
        
        return dummy.next

list1 = construct([5,6,7,8])
list2 = construct([1,2,3,4])

sol = Solution()
sol.mergeTwoLists(list1, list2).printListNode()