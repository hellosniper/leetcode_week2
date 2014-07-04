# N-Queens.py

# Question:  The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#            Given an integer n, return all distinct solutions to the n-queens puzzle.
#            Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' 
#            both indicate a queen and an empty space respectively.
#           
# Question from: https://oj.leetcode.com/problems/n-queens/
# Sulotion:  iteratively read the relation between the ajacent ratings: < = >

# Author: DongDing 
# Date: 2014/07/03
# Time complexity:  O(n^n)
# space complexity:  O(1)  
# Tag: # Recursion # bitwise operation 
# Comment: 
#
from copy import deepcopy
class Solution:
    # @return a list of lists of string
    #def __init__(self):
        #self.result = []
    
    def solveNQueens(self, n):
        self.full = (1<<n) -1
        self.ans = 0
        rownumber = 0
        self.result = []
        self.n = n
        temp = [0 for i in range(n)]
        self.setInRow(temp,rownumber, 0,0,0)
        #print "number of answers",self.ans
        return self.result
        

    def setInRow(self,temp_result,rownumber,c,l,r):
        if c == self.full: # every column is occupied 
            self.ans += 1
            #print 'temp_result', temp_result
            temp = []
            temp.extend(temp_result)
            self.result.append(temp)
            #print self.result
            return
            
        pos = self.full & (~(c|l|r)) # available position in the row, represented by "1"
        #rownumber += 1 
        while (pos):
            p = pos & (-pos)  # return the right most 1 
            pos -= p
            # append []
            position_string =  self.getstr(p)
            temp_result[rownumber] = position_string
            #print "every time",temp_result
            self.setInRow(temp_result, rownumber+1, c+p,(l+p)<<1,(r+p)>>1)
        
    def getstr(self,p):
        str1 = ""
        for i in range(self.n):
            if (p>>i) & 1:
                str1 += "Q"
            else:
                str1 += "."
        return str1    
                
        #if c == self.full:
            #self.ans
            #pass
        
        #pos = self.full & ~(c|l|r)  # availabe position
        #while (pos):
            #rownumber += 1
            #self.setInRow(rownumber, c+p,(l+p)<<1,(r+p)>>1)
a = Solution()
print a.solveNQueens(4)
print a.solveNQueens(8)
print a.getstr(16)
