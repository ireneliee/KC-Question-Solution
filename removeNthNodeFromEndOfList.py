class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)

        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n = n - 1
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

    def printOut(self, head):
        com = ""

        while head != None:
            com = com + " --> " + str(head.val)
            head = head.next

        print(com)

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

s.printOut(one)

s.printOut(s.removeNthFromEnd(one, 2))


        

