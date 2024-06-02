class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_node_l1 = l1
        current_node_l2 = l2
        add_one = 0
        head = ListNode()
        result_node = head

        while current_node_l1 or current_node_l2 or add_one:
            value = add_one
            if current_node_l1:
                value += current_node_l1.val
                current_node_l1 = current_node_l1.next
            if current_node_l2:
                value += current_node_l2.val
                current_node_l2 = current_node_l2.next

            add_one = value // 10
            value %= 10

            head.next = ListNode(value)
            head = head.next

        return result_node.next

# Example usage:
a = ListNode(9)
a.next = ListNode(2)
a.next.next = ListNode(3)
b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)

mySolution = Solution()
current = mySolution.addTwoNumbers(a, b)
while current:
    print(current.val)
    current = current.next

