# Remove Duplicates from Sorted List.py 

# Question: Given a sorted linked list, delete all duplicates such that each element appear only once.
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Question from: https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
# Sulotion:  

# Author: DongDing 
# Date: 2014/07/06
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag: # linked list # pointer  
# Comment: 
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def setbeforehead(self,x):
        node = ListNode(x)
        node.next = self
        return node
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        first = head
        while first.next != None:
            second = first.next
            while second != None:
                if second.val == first.val:
                    second = second.next
                else:
                    break
            if second == None:
                first.next = None
            else:
                first.next = second
                first = second
        return head

node_1 = ListNode(2)
node_1 = node_1.setbeforehead(1)

node_ = node_1
while (node_!= None):
    print node_.val
    node_ = node_.next    

a= Solution()
node = a.deleteDuplicates(node_1)
print node
