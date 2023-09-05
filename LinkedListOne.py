
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        oddTemp,evenTemp, evenHead = ListNode(), ListNode(), ListNode()
        oddHead = oddTemp
        evenHead = evenTemp
        
        count = 0
        
        while temp is not None:
            count = count + 1
           
            if count % 2 == 1:
               
                
                oddTemp.next = temp
                oddTemp = temp
            else:
               
                evenTemp.next = temp
                evenTemp = temp
                
            temp = temp.next
        
        if oddTemp.next is not None:
            oddTemp.next = None
        
        if evenTemp.next is not None:
            evenTemp.next = None
            
    
        oddTemp.next = evenHead.next
        

        
        return oddHead.next