class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


a = ListNode(5)
a.next = ListNode(2)
a.next.next = ListNode(3)
b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)
'''
current = a
while current:
  print(current.val)
  current = current.next
'''

class Solution:
  def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
    current_node_l1 = l1
    current_node_l2 = l2
    add_one = 0

    while current_node_l1 or current_node_l2:
      try:
        head
      except:
        head = ListNode()
        result_node = head
      else:
        head.next = ListNode()

      if current_node_l1 == None:
        head.val = current_node_l2.val + add_one
        add_one = 0
      elif current_node_l2 == None:
        head.val = current_node_l1.val + add_one
        add_one = 0
      else:
        if current_node_l1.val + current_node_l2.val > 9:
          head.val = current_node_l1.val + current_node_l2.val - 10 + add_one
          add_one = 1
        else:
          head.val = current_node_l1.val + current_node_l2.val + add_one
          add_one = 0

      current_node_l1 = current_node_l1.next
      current_node_l2 = current_node_l2.next
    head.next = None
    return result_node


mySolution = Solution()
current = mySolution.addTwoNumbers(a,b)
while current:
  print(current.val)
  current = current.next
