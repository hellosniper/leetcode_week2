# Pow.py

# 
# Question:  Implement pow(x, n).

#           
# Question from: https://oj.leetcode.com/problems/powx-n/
# Sulotion:  x^n = (x*x)^ flour(n/2) *x^(n%2)

# Author: DongDing 
# Date: 2014/07/03
# Time complexity:  O(log(n))
# space complexity:  O(log(n))  
# Tag: # Recursion 
# Comment: 
#

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        #return x**n
        if n == 0: 
            return 1
        if n > 0: 
            return self.computePower(x,n)
        
        if n < 0:
            return float(1)/self.computePower(x,-n)
    
    def computePower(self,x, n):
        # @param x, a float
        # @param n, a positive integer
        # @return a float  
        # if n == 0:
        #     return 1
        if n == 1: #Base case
            return x
        
        div = n/2
        if n%2 == 1:
            return self.computePower(x*x,div)*x
        else:
            return self.computePower(x*x,div)
            
a= Solution()
print a.pow(2, -10)* a.pow(2, 9)
