from typing import Optional
# From: https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    This solution takes O(n) in time and O(1) in space.
    """
    def convertToList(self, head: Optional[ListNode]) -> [int]:
        l = []
        node = head
        while(node != None):
            l.append(node.val)
            node = node.next
        return l

    def calculateLen(self, head: Optional[ListNode]) -> int:
        if head == None:
            return 0
        
        count = 1
        node = head
        while(node.next != None):
            count = count + 1
            node = node.next
        return count

    def isPalindromeList(self, l:[int]) -> bool:
        """
        | 1 | 2 | 3 | 4 |  4  | 3 | 2 | 1 |
         i-3 i-2 i-1  i  mid/j j+1 j+2 j+3
        """
        
        n = len(l)
        mid = int(n/2)
        i = None
        j = None
        
        if n == 1 or n == 0:
            return True
        if n == 2:
            return l[0] == l[1]
        
        if n % 2 == 0:
            i = mid -1
            j = mid
            
            for k in range(mid):
                if l[i] != l[j]:
                    return False
                i = i-1
                j = j+1
            return True
        else:
            i = mid - 1
            j = mid + 1
            
            for k in range(mid):
                if l[i] != l[j]:
                    return False
                i = i-1
                j = j+1
            return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = self.convertToList(head)
        return self.isPalindromeList(l)
        
        
#Tests
def testSimpleLists():

    s = Solution()

    result = s.isPalindromeList([1])
    assert(result == True)

    result = s.isPalindromeList([1,1])
    assert(result == True)
    
    result = s.isPalindromeList([1,2,2,1])
    assert(result == True)

    result = s.isPalindromeList([1,2])
    assert(result == False)
    
    result = s.isPalindromeList([1,2,3,2,1])
    assert(result == True)  

    result = s.isPalindromeList([1,2,3,3,1])
    assert(result == False)


if __name__ == "__main__":
    testSimpleLists()
