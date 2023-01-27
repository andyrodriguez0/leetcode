
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head):

    slow = head
    fast = head
    count = 0

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        count += 2
    
    mid = slow
    first = mid.next
    second = mid.next.next

    first.next = None

    while second:

        next_node = second.next
        second.next = first

        first = second
        second = next_node
    
    mid.next = first

    slow = head
    fast = head

    if not count:
        fast = fast.next
    else:
        for i in range(count):
            fast = fast.next

    print(count, slow.val, fast.val)
    ans = slow.val + fast.val

    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        ans = max(slow.val + fast.val, ans)

    return ans