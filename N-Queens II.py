# N-Queens II.py#

# Question: Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.
#           
# Question from: https://oj.leetcode.com/problems/n-queens-ii/
# Sulotion:  iteratively read the relation between the ajacent ratings: < = >

# Author: DongDing 
# Date: 2014/07/02
# Time complexity:  O(n^n)
# space complexity:  O(1)  
# Tag: # Recursion # bitwise operation 
# Comment: 
class Solution:
    ans, full = 0, 0
    # @return an integer
    def totalNQueens(self, n):
        
        self.full = (1<<n) -1 # 
        self.setInRow(0,0,0)
        
    def setInRow(self, c, l, r):
        if c == self.full: # every column is occupied 
            self.ans+=1
            return
        pos = self.full & (~(c|l|r)) # available position in the row, represented by "1" 
        while (pos):
            p = pos & (-pos)  # return the right most 1 
            pos -= p
            self.setInRow(c+p,(l+p)<<1,(r+p)>>1)
