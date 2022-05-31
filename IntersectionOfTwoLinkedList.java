
public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> record = new HashSet<>();
        
        ListNode temp = headA;
        
        while (temp != null) {
            record.add(temp);
            temp = temp.next;
        }
        
        ListNode temp1 = headB;
        
        while (temp1 != null) {
            if(record.contains(temp1)) {
                return temp1;
            } else {
                temp1 = temp1.next;
            }
        }
        
        return null;
    }
}