
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        # make sure more than two
        if (not head) or (not head.next):
            return head
        
        odd_head = head
        even_head = head.next

        currNode = head
        nextNode = head

        while currNode:
            nextNode = currNode.next
            if currNode.next and currNode.next:
                currNode.next = currNode.next.next
            currNode = nextNode

        print('Odd head is ...')
        printNode(odd_head)
        print('Even head is ...')
        printNode(even_head)

        fullNodeCounter = odd_head

        while fullNodeCounter.next:
            fullNodeCounter = fullNodeCounter.next

        
        fullNodeCounter.next = even_head 

        return odd_head




s = Solution()
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five

def printNode(curr):
    result = ""
    while curr:
        result = result + " -> " + str(curr.val)
        curr = curr.next
    
    print(result)

printNode(s.oddEvenList(one))



        