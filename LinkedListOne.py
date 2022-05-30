
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        oddTemp, oddHead, evenTemp, evenHead = ListNode(), ListNode(), ListNode(), ListNode()
        oddHead = oddTemp
        evenHead = evenTemp
        
        count = 0
        
        while temp is not None:
            count = count + 1
            print('at count' + str(count))
            if count % 2 == 1:
                print('current oddTemp is ' + str(oddTemp.val))
                print('adding ' + str(temp.val) + 'into the odd list')
                
                oddTemp.next = temp
                oddTemp = temp
            else:
                print('current oddEven is ' + str(evenTemp.val))
                print('adding ' + str(temp.val) + 'into the even list')
                evenTemp.next = temp
                evenTemp = temp
                
            temp = temp.next
        
        print('Odd node')
        o = oddHead
        while o is not None:
            print(str(o.val) + ('-->'))
            o = o.next
            
        print('Even node')
        o = evenHead
        while o is not None:
            print(str(o.val) + ('-->'))
            
            o = o.next
        print('oddTemp is ' + str(oddTemp.val))
        oddTemp.next = evenHead.next
        

        
        return oddHead.next