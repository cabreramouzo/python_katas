"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
https://leetcode.com/problems/add-two-numbers/
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseStr(self, str):
          s = ""
          for c in reversed(str):
            s += c
          return s
    
    def reverseListNodeToInt(self, l: Optional[ListNode]) -> int:
      
      strNumber = ""
      current = l
      while(current != None):
        strNumber = strNumber + str(current.val)
        current = current.next
      return int(self.reverseStr(strNumber))

    def convertToListNode(self, s: str) -> Optional[ListNode]:

      numStr = s
      n = len(numStr)
      node = ListNode()
      head = node

      for i in range(n-1):
        node.val = numStr[i]
        node.next = ListNode()
        node = node.next

      node.val = numStr[-1]
      node.next = None

      return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      
      n1 = self.reverseListNodeToInt(l1)
      n2 = self.reverseListNodeToInt(l2)
      res = (n1+n2)
      res = str(res)
      res = self.reverseStr(res)
      return self.convertToListNode(res)


def tests():

  s = Solution()
  n1 = "243"
  n2 = "564"
  l1 = s.convertToListNode(n1)
  l2 = s.convertToListNode(n2)
  res = s.addTwoNumbers(l1,l2)
  expected = s.convertToListNode("708")
  expected = s.reverseListNodeToInt(expected)
  res = s.reverseListNodeToInt(res)
  assert(expected == res)



if __name__ == "__main__":

  tests()



