# Definition for singly-linked list.
def print_node(head):
    text = ""
    curr = head
    while curr != None:
        text = text + " --> " + str(curr.val)
        curr = curr.next 
    print(text)
        
class ListNode(object):
    def __init__(self, val=0, next=None): 
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):

        if not head:
            return None
        
        pointer = head
        prev = head
        
        if head.next:
            head = head.next

        while pointer and pointer.next:
            print('Curr pointer is ', str(pointer.val))
            firstNode = pointer
            print('First val is ', str(firstNode.val))
            secondNode = pointer.next
            print('Second val is ', str(secondNode.val))

            prev.next = secondNode

            firstNode.next = firstNode.next.next
            secondNode.next = firstNode

            prev = firstNode

            pointer = pointer.next
        
        return head



s = Solution()
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
three.next = four
print('Before solution')
print_node(one)
# s.swapPairs(one)

print('After solution')
print_node(s.swapPairs(one))