# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printListNode(self):
        k = self
        print('Printing list node')
        while k is not None:
            print('Listnode ' + str(k.val) + '-->')
            k = k.next
    

def construct(lis: List[int]) -> ListNode:
    dummy = ListNode()
    pointer = dummy
    for i in range(len(lis)):
        pointer.next = ListNode(lis[i])
        pointer = pointer.next
    return dummy.next



