
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):

    dummy = head
    count = 0

    while dummy and dummy.next:

        first = dummy.next
        second = dummy

        if not count:
            head = first
        else:
            last.next = first

        third = first.next
        first.next = second
        second.next = third

        last = second
        dummy = dummy.next
        count += 1

    return head