# Remove Duplicates from Sorted List II.py

# Question:  # Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#           
# Question from: https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
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

# Solution: pointer first points to the first distinct value
# pointer duplicate points duplicate
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
        # set head to be the fisrt distinct node
        if head == None:
            return None
        while head.next != None:#head.val == head.next.val:
            #delete the dupicates at the head
            if head.val != head.next.val:
                break
            #
            second = head.next
            while second != None: # find the one that != head.val
                if second.val == head.val:
                    second = second.next
                else:
                    break
                
            if second == None:
                return None
            else:
                head = second  #delete the dupicates at the head
        if head.next == None:
            return head
        
        # delete the dupicates  after head      
        first = head.next
        prefirst = head
        while first.next != None:
            
            if first.val != first.next.val:
                prefirst = first
                first = first.next
                
                continue
            #
            second = first.next
            while second != None:
                if second.val == first.val:
                    second = second.next
                else:
                    break
            #delete the dupicates between first and second    
            if second == None:
                prefirst.next = None
                break
            else:  
                first = second         
                prefirst.next = first
        return head
node_1 = ListNode(1)
node_1 = node_1.setbeforehead(1)

node_ = node_1
while (node_!= None):
    print node_.val
    node_ = node_.next    
    
a= Solution()
node = a.deleteDuplicates(node_1)
print node
